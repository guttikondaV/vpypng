from datetime import datetime, timezone
from io import BufferedIOBase, BytesIO
from struct import unpack

from .crc import check_crc_is_same
from .exceptions import PNGDecodeException
from .PNGImage import PNGImage


class PNGDecoder:
    @staticmethod
    def decode(file: BufferedIOBase):
        decoder = PNGDecoder(file)
        return decoder.image

    def __init__(self, file: BufferedIOBase):
        # Required variables
        self.file = file
        self.image = PNGImage()
        self.keep_decoding = True

        # Start decoding
        self._check_file_signature()

        while self.keep_decoding:
            chunk_type, chunk, chunk_size = self._read_chunk_and_check_crc()

            self._do_chunk_parsing(chunk_type, chunk, chunk_size)

    # CRITICAL CHUNKS PARSING SECTION START
    def _parse_IHDR(self, chunk, chunk_size):
        print("Found IHDR chunk")  # Remove after defining all chunks
        width = unpack(">I", chunk.read(4))[0]
        height = unpack(">I", chunk.read(4))[0]
        bit_depth = self._parse_int_from_byte(chunk.read(1))
        color_type = self._parse_int_from_byte(chunk.read(1))
        compression_method = self._parse_int_from_byte(chunk.read(1))
        filter_method = self._parse_int_from_byte(chunk.read(1))
        interlace_method = self._parse_int_from_byte(chunk.read(1))

        self.image.set_items_from_map(
            {
                "width": width,
                "height": height,
                "bit_depth": bit_depth,
                "color_type": color_type,
                "compression_method": compression_method,
                "filter_method": filter_method,
                "interlace_method": interlace_method,
            }
        )

    def _parse_PLTE(self, chunk, chunk_size):
        print("Found PLTE chunk")  # Remove after defining all chunks
        pass

    def _parse_IDAT(self, chunk, chunk_size):
        print("Found IDAT chunk")  # Remove after defining all chunks
        pass

    def _parse_IEND(self, chunk, chunk_size):
        print("Found IEND chunk")  # Remove after defining all chunks
        self.keep_decoding = False

    # CRITICAL CHUNKS PARSING SECTION END

    # ANCILLARY CHUNKS PARSING SECTION START
    def _parse_CHRM(self, chunk, chunk_size):
        print("Found CHRM chunk")  # Remove after defining all chunks
        pass

    def _parse_GAMA(self, chunk, chunk_size):
        print("Found GAMA chunk")  # Remove after defining all chunks
        pass

    def _parse_ICCP(self, chunk, chunk_size):
        print("Found ICCP chunk")  # Remove after defining all chunks
        pass

    def _parse_SBIT(self, chunk, chunk_size):
        print("Found SBIT chunk")  # Remove after defining all chunks
        pass

    def _parse_SRGB(self, chunk, chunk_size):
        print("Found SRGB chunk")  # Remove after defining all chunks
        pass

    def _parse_BKGD(self, chunk, chunk_size):
        print("Found BKGD chunk")  # Remove after defining all chunks
        pass

    def _parse_HIST(self, chunk, chunk_size):
        print("Found HIST chunk")  # Remove after defining all chunks
        pass

    def _parse_TRNS(self, chunk, chunk_size):
        print("Found TRNS chunk")  # Remove after defining all chunks
        pass

    def _parse_PHYS(self, chunk, chunk_size):
        print("Found PHYS chunk")  # Remove after defining all chunks
        pass

    def _parse_SPLT(self, chunk, chunk_size):
        print("Found SPLT chunk")  # Remove after defining all chunks
        pass

    def _parse_TIME(self, chunk, chunk_size):
        print("Found TIME chunk")  # Remove after defining all chunks
        try:

            year = self._parse_int_from_byte(chunk.read(2))
            month = self._parse_int_from_byte(chunk.read(1))
            day = self._parse_int_from_byte(chunk.read(1))
            hour = self._parse_int_from_byte(chunk.read(1))
            minute = self._parse_int_from_byte(chunk.read(1))
            second = self._parse_int_from_byte(chunk.read(1))

            if second >= 60:
                second = 59

            date_of_last_modification = datetime(
                year, month, day, hour, minute, second, tzinfo=timezone.utc
            )

            self.image["last_modified"] = date_of_last_modification
        except Exception as e:
            return

    def _parse_TEXT(self, chunk, chunk_size):
        print("Found TEXT chunk")  # Remove after defining all chunks
        ALLOWED_KEYWORDS = [
            keyword.title()
            for keyword in [
                "title",
                "author",
                "description",
                "copyright",
                "creation time",
                "software",
                "disclaimer",
                "warning",
                "source",
                "comment",
            ]
        ] + ["XML:com.adobe.xmp"]
        
        try:
            parsed_bytes, null_is_found = 0, False
            key_word, value = "", ""

            while not null_is_found and parsed_bytes < chunk_size:
                character = self._parse_int_from_byte(chunk.read(1))
                if character == 0:
                    parsed_bytes += 1
                    break
                key_word += chr(character)

                parsed_bytes += 1

            if key_word not in ALLOWED_KEYWORDS:
                return

            remaining_bytes = chunk_size - parsed_bytes

            for i in range(remaining_bytes):
                character = self._parse_int_from_byte(chunk.read(1))
                value += chr(character)

            if self.image["text_data"] is None:
                self.image["text_data"] = {}
                self.image["text_data"][key_word] = value

            else:
                self.image["text_data"][key_word] = value
        except Exception as e:
            print(e.args)
            return

    def _parse_ZTXT(self, chunk, chunk_size):
        print("Found ZTXT chunk")  # Remove after defining all chunks
        pass

    def _parse_ITXT(self, chunk, chunk_size):
        print("Found ITXT chunk")  # Remove after defining all chunks
        pass

    # ANCILLARY CHUNKS PARSING SECTION END

    # HELPER CHUNKS SECTION START
    def _check_file_signature(self):
        first_bytes = self.file.read(8)
        if [int(x) for x in first_bytes] != PNGImage.PNG_FILE_SIGNATURE:
            raise PNGDecodeException

    def _read_chunk_and_check_crc(self):
        chunk_size = unpack(">I", self.file.read(4))[0]

        chunk_header = self.file.read(4)

        chunk = self.file.read(chunk_size)

        chunk_crc = unpack(">I", self.file.read(4))[0]

        data_to_check_crc = chunk_header + chunk

        if not check_crc_is_same(data_to_check_crc, chunk_crc):
            raise PNGDecodeException

        chunk_header = [int(x) for x in chunk_header]
        return chunk_header, BytesIO(chunk), chunk_size

    def _do_chunk_parsing(self, chunk_header, chunk, chunk_size):
        # CRITICAL CHUNKS PARSING SECTION START
        if chunk_header == PNGImage.PNG_IHDR_CHUNK_SIGNATURE:
            self._parse_IHDR(chunk, chunk_size)
        elif chunk_header == PNGImage.PNG_PLTE_CHUNK_SIGNATURE:
            self._parse_PLTE(chunk, chunk_size)
        elif chunk_header == PNGImage.PNG_IDAT_CHUNK_SIGNATURE:
            self._parse_IDAT(chunk, chunk_size)
        elif chunk_header == PNGImage.PNG_IEND_CHUNK_SIGNATURE:
            self._parse_IEND(chunk, chunk_size)
        # CRITICAL CHUNKS PARSING SECTION END

        # ANCILLARY CHUNKS PARSING SECTION START
        elif chunk_header == PNGImage.PNG_CHRM_CHUNK_SIGNATURE:
            self._parse_CHRM(chunk, chunk_size)
        elif chunk_header == PNGImage.PNG_GAMA_CHUNK_SIGNATURE:
            self._parse_GAMA(chunk, chunk_size)
        elif chunk_header == PNGImage.PNG_ICCP_CHUNK_SIGNATURE:
            self._parse_ICCP(chunk, chunk_size)
        elif chunk_header == PNGImage.PNG_SBIT_CHUNK_SIGNATURE:
            self._parse_SBIT(chunk, chunk_size)
        elif chunk_header == PNGImage.PNG_SRGB_CHUNK_SIGNATURE:
            self._parse_SRGB(chunk, chunk_size)
        elif chunk_header == PNGImage.PNG_BKGD_CHUNK_SIGNATURE:
            self._parse_BKGD(chunk, chunk_size)
        elif chunk_header == PNGImage.PNG_HIST_CHUNK_SIGNATURE:
            self._parse_HIST(chunk, chunk_size)
        elif chunk_header == PNGImage.PNG_TRNS_CHUNK_SIGNATURE:
            self._parse_TRNS(chunk, chunk_size)
        elif chunk_header == PNGImage.PNG_PHYS_CHUNK_SIGNATURE:
            self._parse_PHYS(chunk, chunk_size)
        elif chunk_header == PNGImage.PNG_SPLT_CHUNK_SIGNATURE:
            self._parse_SPLT(chunk, chunk_size)
        elif chunk_header == PNGImage.PNG_TIME_CHUNK_SIGNATURE:
            self._parse_TIME(chunk, chunk_size)
        elif chunk_header == PNGImage.PNG_TEXT_CHUNK_SIGNATURE:
            self._parse_TEXT(chunk, chunk_size)
        elif chunk_header == PNGImage.PNG_ZTXT_CHUNK_SIGNATURE:
            self._parse_ZTXT(chunk, chunk_size)
        elif chunk_header == PNGImage.PNG_ITXT_CHUNK_SIGNATURE:
            self._parse_ITXT(chunk, chunk_size)
        # ANCILLARY CHUNKS PARSING SECTION END

    def _parse_int_from_byte(self, bytes):
        return int.from_bytes(bytes, byteorder="big")

    # HELPER CHUNKS SECTION END

    pass
