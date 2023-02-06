from io import BufferedIOBase
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
        pass

    def _parse_PLTE(self, chunk, chunk_size):
        pass

    def _parse_IDAT(self, chunk, chunk_size):
        pass

    def _parse_IEND(self, chunk, chunk_size):
        pass

    # CRITICAL CHUNKS PARSING SECTION END

    # ANCILLARY CHUNKS PARSING SECTION START
    def _parse_CHRM(self, chunk, chunk_size):
        pass

    def _parse_GAMA(self, chunk, chunk_size):
        pass

    def _parse_ICCP(self, chunk, chunk_size):
        pass

    def _parse_SBIT(self, chunk, chunk_size):
        pass

    def _parse_SRGB(self, chunk, chunk_size):
        pass

    def _parse_BKGD(self, chunk, chunk_size):
        pass

    def _parse_HIST(self, chunk, chunk_size):
        pass

    def _parse_TRNS(self, chunk, chunk_size):
        pass

    def _parse_PHYS(self, chunk, chunk_size):
        pass

    def _parse_SPLT(self, chunk, chunk_size):
        pass

    def _parse_TIME(self, chunk, chunk_size):
        pass

    def _parse_TEXT(self, chunk, chunk_size):
        pass

    def _parse_ZTXT(self, chunk, chunk_size):
        pass

    def _parse_ITXT(self, chunk, chunk_size):
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
        return chunk_header, chunk, chunk_size

    def _do_chunk_parsing(self, chunk_header, chunk, chunk_size):
        # CRITICAL CHUNKS PARSING SECTION START
        if chunk_header == PNGImage.IHDR_CHUNK_HEADER:
            self._parse_IHDR(chunk, chunk_size)
        elif chunk_header == PNGImage.PLTE_CHUNK_HEADER:
            self._parse_PLTE(chunk, chunk_size)
        elif chunk_header == PNGImage.IDAT_CHUNK_HEADER:
            self._parse_IDAT(chunk, chunk_size)
        elif chunk_header == PNGImage.IEND_CHUNK_HEADER:
            self._parse_IEND(chunk, chunk_size)
        # CRITICAL CHUNKS PARSING SECTION END

        # ANCILLARY CHUNKS PARSING SECTION START
        elif chunk_header == PNGImage.CHRM_CHUNK_HEADER:
            self._parse_CHRM(chunk, chunk_size)
        elif chunk_header == PNGImage.GAMA_CHUNK_HEADER:
            self._parse_GAMA(chunk, chunk_size)
        elif chunk_header == PNGImage.ICCP_CHUNK_HEADER:
            self._parse_ICCP(chunk, chunk_size)
        elif chunk_header == PNGImage.SBIT_CHUNK_HEADER:
            self._parse_SBIT(chunk, chunk_size)
        elif chunk_header == PNGImage.SRGB_CHUNK_HEADER:
            self._parse_SRGB(chunk, chunk_size)
        elif chunk_header == PNGImage.BKGD_CHUNK_HEADER:
            self._parse_BKGD(chunk, chunk_size)
        elif chunk_header == PNGImage.HIST_CHUNK_HEADER:
            self._parse_HIST(chunk, chunk_size)
        elif chunk_header == PNGImage.TRNS_CHUNK_HEADER:
            self._parse_TRNS(chunk, chunk_size)
        elif chunk_header == PNGImage.PHYS_CHUNK_HEADER:
            self._parse_PHYS(chunk, chunk_size)
        elif chunk_header == PNGImage.SPLT_CHUNK_HEADER:
            self._parse_SPLT(chunk, chunk_size)
        elif chunk_header == PNGImage.TIME_CHUNK_HEADER:
            self._parse_TIME(chunk, chunk_size)
        elif chunk_header == PNGImage.TEXT_CHUNK_HEADER:
            self._parse_TEXT(chunk, chunk_size)
        elif chunk_header == PNGImage.ZTXT_CHUNK_HEADER:
            self._parse_ZTXT(chunk, chunk_size)
        elif chunk_header == PNGImage.ITXT_CHUNK_HEADER:
            self._parse_ITXT(chunk, chunk_size)
        # ANCILLARY CHUNKS PARSING SECTION END

    # HELPER CHUNKS SECTION END

    pass