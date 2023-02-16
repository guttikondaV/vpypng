import glob
from pathlib import Path

import png
import pytest

from vpypng import PNGCodec, PNGDecodeException, PNGDecoder


class TestPngDecoder:
    def test_decoder_exists(self):
        assert PNGDecoder is not None

    def test_decoder_input_file_signature_ok_input_str(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            decoded_image = PNGCodec.decode(good_image_path)
            assert decoded_image is not None

    def test_decoder_input_file_signature_ok_input_path(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            decoded_image = PNGCodec.decode(Path(good_image_path))
            assert decoded_image is not None

    def test_decoder_input_file_signature_ok_input_file(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            with open(good_image_path, "rb") as pngfile:
                decoded_image = PNGCodec.decode(pngfile)
                assert decoded_image is not None

    def test_decoder_input_file_signature_ok_input_bytes(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            with open(good_image_path, "rb") as pngfile:
                decoded_image = PNGCodec.decode(pngfile.read())
                assert decoded_image is not None

    def test_decoder_input_file_signature_bad_input_str(self):
        BAD_SIGNATURE_PATHS = [
            "./tests/testimages/bad_signature_empty.png",
            "./tests/testimages/bad_signature_mismatch-truncated.png",
            "./tests/testimages/bad_signature_mismatch.png",
            "./tests/testimages/bad_signature_truncated.png",
        ]

        for bad_signature_path in BAD_SIGNATURE_PATHS:
            pytest.raises(PNGDecodeException, PNGCodec.decode, bad_signature_path)

    def test_decoder_input_file_signature_bad_input_path(self):
        BAD_SIGNATURE_PATHS = [
            "./tests/testimages/bad_signature_empty.png",
            "./tests/testimages/bad_signature_mismatch-truncated.png",
            "./tests/testimages/bad_signature_mismatch.png",
            "./tests/testimages/bad_signature_truncated.png",
        ]

        for bad_signature_path in BAD_SIGNATURE_PATHS:
            pytest.raises(PNGDecodeException, PNGCodec.decode, Path(bad_signature_path))

    def test_decoder_input_file_signature_bad_input_file(self):
        BAD_SIGNATURE_PATHS = [
            "./tests/testimages/bad_signature_empty.png",
            "./tests/testimages/bad_signature_mismatch-truncated.png",
            "./tests/testimages/bad_signature_mismatch.png",
            "./tests/testimages/bad_signature_truncated.png",
        ]

        for bad_signature_path in BAD_SIGNATURE_PATHS:
            with open(bad_signature_path, "rb") as pngfile:
                pytest.raises(PNGDecodeException, PNGCodec.decode, pngfile)

    def test_decoder_input_file_signature_bad_input_bytes(self):
        BAD_SIGNATURE_PATHS = [
            "./tests/testimages/bad_signature_empty.png",
            "./tests/testimages/bad_signature_mismatch-truncated.png",
            "./tests/testimages/bad_signature_mismatch.png",
            "./tests/testimages/bad_signature_truncated.png",
        ]

        for bad_signature_path in BAD_SIGNATURE_PATHS:
            with open(bad_signature_path, "rb") as pngfile:
                pytest.raises(PNGDecodeException, PNGCodec.decode, pngfile.read())

    def test_decoder_ihdr_ok_input_str(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            decoded_image = PNGCodec.decode(good_image_path)
            standard_decoded_image = png.Reader(filename=good_image_path).read()

            assert decoded_image.width == standard_decoded_image[0]
            assert decoded_image.height == standard_decoded_image[1]
            assert decoded_image.bit_depth == standard_decoded_image[-1]["bitdepth"]
            assert (
                decoded_image.interlace_method
                == standard_decoded_image[-1]["interlace"]
            )

    def test_decoder_ihdr_ok_input_path(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            decoded_image = PNGCodec.decode(Path(good_image_path))
            standard_decoded_image = png.Reader(filename=good_image_path).read()

            assert decoded_image.width == standard_decoded_image[0]
            assert decoded_image.height == standard_decoded_image[1]
            assert decoded_image.bit_depth == standard_decoded_image[-1]["bitdepth"]
            assert (
                decoded_image.interlace_method
                == standard_decoded_image[-1]["interlace"]
            )

    def test_decoder_ihdr_ok_input_file(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            with open(good_image_path, "rb") as pngfile:
                decoded_image = PNGCodec.decode(pngfile)
                standard_decoded_image = png.Reader(filename=good_image_path).read()

                assert decoded_image.width == standard_decoded_image[0]
                assert decoded_image.height == standard_decoded_image[1]
                assert decoded_image.bit_depth == standard_decoded_image[-1]["bitdepth"]
                assert (
                    decoded_image.interlace_method
                    == standard_decoded_image[-1]["interlace"]
                )

    def test_decoder_ihdr_ok_input_bytes(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            with open(good_image_path, "rb") as pngfile:
                decoded_image = PNGCodec.decode(pngfile.read())
                standard_decoded_image = png.Reader(filename=good_image_path).read()

                assert decoded_image.width == standard_decoded_image[0]
                assert decoded_image.height == standard_decoded_image[1]
                assert decoded_image.bit_depth == standard_decoded_image[-1]["bitdepth"]
                assert (
                    decoded_image.interlace_method
                    == standard_decoded_image[-1]["interlace"]
                )

    def test_decoder_time_ok_input_str(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_time*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            decoded_image = PNGCodec.decode(good_image_path)

            assert decoded_image["last_modified"] is not None

    def test_decoder_time_ok_input_path(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_time*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            decoded_image = PNGCodec.decode(Path(good_image_path))

            assert decoded_image["last_modified"] is not None

    def test_decoder_time_ok_input_file(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_time*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            with open(good_image_path, "rb") as pngfile:
                decoded_image = PNGCodec.decode(pngfile)

                assert decoded_image["last_modified"] is not None

    def test_decoder_time_ok_input_bytes(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_time*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            with open(good_image_path, "rb") as pngfile:
                decoded_image = PNGCodec.decode(pngfile.read())

                assert decoded_image["last_modified"] is not None

    def test_decoder_time_bad_input_str(self):
        BAD_IMAGES_PATHS = glob.glob("./tests/testimages/bad_time*.png")
        for bad_image_path in BAD_IMAGES_PATHS:
            decoded_image = PNGCodec.decode(bad_image_path)

            assert decoded_image["last_modified"] is None

    def test_decoder_time_bad_input_path(self):
        BAD_IMAGES_PATHS = glob.glob("./tests/testimages/bad_time*.png")
        for bad_image_path in BAD_IMAGES_PATHS:
            decoded_image = PNGCodec.decode(Path(bad_image_path))

            assert decoded_image["last_modified"] is None

    def test_decoder_time_bad_input_file(self):
        BAD_IMAGES_PATHS = glob.glob("./tests/testimages/bad_time*.png")
        for bad_image_path in BAD_IMAGES_PATHS:
            with open(bad_image_path, "rb") as pngfile:
                decoded_image = PNGCodec.decode(pngfile)

                assert decoded_image["last_modified"] is None

    def test_decoder_time_bad_input_bytes(self):
        BAD_IMAGES_PATHS = glob.glob("./tests/testimages/bad_time*.png")
        for bad_image_path in BAD_IMAGES_PATHS:
            with open(bad_image_path, "rb") as pngfile:
                decoded_image = PNGCodec.decode(pngfile.read())

                assert decoded_image["last_modified"] is None

    def test_decoder_text_ok_input_str(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_text*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            decoded_image = PNGCodec.decode(good_image_path)

            assert decoded_image["text_data"] is not None
            assert len(list(decoded_image["text_data"].keys())) > 0

    def test_decoder_text_ok_input_path(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_text*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            decoded_image = PNGCodec.decode(Path(good_image_path))

            assert decoded_image["text_data"] is not None
            assert len(list(decoded_image["text_data"].keys())) > 0

    def test_decoder_text_ok_input_file(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_text*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            with open(good_image_path, "rb") as pngfile:
                decoded_image = PNGCodec.decode(pngfile)

                assert decoded_image["text_data"] is not None
                assert len(list(decoded_image["text_data"].keys())) > 0

    def test_decoder_text_ok_input_bytes(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_text*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            with open(good_image_path, "rb") as pngfile:
                decoded_image = PNGCodec.decode(pngfile.read())

                assert decoded_image["text_data"] is not None
                assert len(list(decoded_image["text_data"].keys())) > 0

    def test_decoder_text_bad_input_str(self):
        BAD_IMAGES_PATHS = glob.glob("./tests/testimages/bad_text*.png")
        for bad_image_path in BAD_IMAGES_PATHS:
            decoded_image = PNGCodec.decode(bad_image_path)

            assert decoded_image["text_data"] is None

    def test_decoder_text_bad_input_path(self):
        BAD_IMAGES_PATHS = glob.glob("./tests/testimages/bad_text*.png")
        for bad_image_path in BAD_IMAGES_PATHS:
            decoded_image = PNGCodec.decode(Path(bad_image_path))

            assert decoded_image["text_data"] is None

    def test_decoder_text_bad_input_file(self):
        BAD_IMAGES_PATHS = glob.glob("./tests/testimages/bad_text*.png")
        for bad_image_path in BAD_IMAGES_PATHS:
            with open(bad_image_path, "rb") as pngfile:
                decoded_image = PNGCodec.decode(pngfile)

                assert decoded_image["text_data"] is None

    def test_decoder_text_bad_input_bytes(self):
        BAD_IMAGES_PATHS = glob.glob("./tests/testimages/bad_text*.png")
        for bad_image_path in BAD_IMAGES_PATHS:
            with open(bad_image_path, "rb") as pngfile:
                decoded_image = PNGCodec.decode(pngfile.read())

                assert decoded_image["text_data"] is None

    def test_decoder_itxt_ok_input_str(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_itxt*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            decoded_image = PNGCodec.decode(good_image_path)

            assert decoded_image["itxt_data"] is not None
            assert len(decoded_image["itxt_data"]) > 0

    def test_decoder_itxt_ok_input_path(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_itxt*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            decoded_image = PNGCodec.decode(Path(good_image_path))

            assert decoded_image["itxt_data"] is not None
            assert len(decoded_image["itxt_data"]) > 0

    def test_decoder_itxt_ok_input_file(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_itxt*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            with open(good_image_path, "rb") as pngfile:
                decoded_image = PNGCodec.decode(pngfile)

                assert decoded_image["itxt_data"] is not None
                assert len(decoded_image["itxt_data"]) > 0

    def test_decoder_itxt_ok_input_bytes(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_itxt*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            with open(good_image_path, "rb") as pngfile:
                decoded_image = PNGCodec.decode(pngfile.read())

                assert decoded_image["itxt_data"] is not None
                assert len(decoded_image["itxt_data"]) > 0

    def test_decoder_itxt_bad_input_str(self):
        BAD_IMAGES_PATHS = glob.glob("./tests/testimages/bad_itxt*.png")
        for bad_image_path in BAD_IMAGES_PATHS:
            decoded_image = PNGCodec.decode(bad_image_path)

            assert decoded_image["itxt_data"] is None

    def test_decoder_itxt_bad_input_path(self):
        BAD_IMAGES_PATHS = glob.glob("./tests/testimages/bad_itxt*.png")
        for bad_image_path in BAD_IMAGES_PATHS:
            decoded_image = PNGCodec.decode(Path(bad_image_path))

            assert decoded_image["itxt_data"] is None

    def test_decoder_itxt_bad_input_file(self):
        BAD_IMAGES_PATHS = glob.glob("./tests/testimages/bad_itxt*.png")
        for bad_image_path in BAD_IMAGES_PATHS:
            with open(bad_image_path, "rb") as pngfile:
                decoded_image = PNGCodec.decode(pngfile)

                assert decoded_image["itxt_data"] is None

    def test_decoder_itxt_bad_input_bytes(self):
        BAD_IMAGES_PATHS = glob.glob("./tests/testimages/bad_itxt*.png")
        for bad_image_path in BAD_IMAGES_PATHS:
            with open(bad_image_path, "rb") as pngfile:
                decoded_image = PNGCodec.decode(pngfile.read())

                assert decoded_image["itxt_data"] is None

    def test_decoder_ztxt_ok_input_str(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_ztxt*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            decoded_image = PNGCodec.decode(good_image_path)

            assert decoded_image["ztxt_data"] is not None
            assert len(list(decoded_image["ztxt_data"].keys())) > 0

    def test_decoder_ztxt_ok_input_path(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_ztxt*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            decoded_image = PNGCodec.decode(Path(good_image_path))

            assert decoded_image["ztxt_data"] is not None
            assert len(list(decoded_image["ztxt_data"].keys())) > 0

    def test_decoder_ztxt_ok_input_file(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_ztxt*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            with open(good_image_path, "rb") as pngfile:
                decoded_image = PNGCodec.decode(pngfile)

                assert decoded_image["ztxt_data"] is not None
                assert len(list(decoded_image["ztxt_data"].keys())) > 0

    def test_decoder_ztxt_ok_input_bytes(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_ztxt*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            with open(good_image_path, "rb") as pngfile:
                decoded_image = PNGCodec.decode(pngfile.read())

                assert decoded_image["ztxt_data"] is not None
                assert len(list(decoded_image["ztxt_data"].keys())) > 0

    def test_decoder_ztxt_bad_input_str(self):
        BAD_IMAGES_PATHS = glob.glob("./tests/testimages/bad_ztxt*.png")
        for bad_image_path in BAD_IMAGES_PATHS:
            decoded_image = PNGCodec.decode(bad_image_path)

            assert decoded_image["ztxt_data"] is None

    def test_decoder_ztxt_bad_input_path(self):
        BAD_IMAGES_PATHS = glob.glob("./tests/testimages/bad_ztxt*.png")
        for bad_image_path in BAD_IMAGES_PATHS:
            decoded_image = PNGCodec.decode(Path(bad_image_path))

            assert decoded_image["ztxt_data"] is None

    def test_decoder_ztxt_bad_input_file(self):
        BAD_IMAGES_PATHS = glob.glob("./tests/testimages/bad_ztxt*.png")
        for bad_image_path in BAD_IMAGES_PATHS:
            with open(bad_image_path, "rb") as pngfile:
                decoded_image = PNGCodec.decode(pngfile)

                assert decoded_image["ztxt_data"] is None

    def test_decoder_ztxt_bad_input_bytes(self):
        BAD_IMAGES_PATHS = glob.glob("./tests/testimages/bad_ztxt*.png")
        for bad_image_path in BAD_IMAGES_PATHS:
            with open(bad_image_path, "rb") as pngfile:
                decoded_image = PNGCodec.decode(pngfile.read())

                assert decoded_image["ztxt_data"] is None

    def test_decoder_phys_ok_input_str(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_phys*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            decoded_image = PNGCodec.decode(good_image_path)

            assert decoded_image["phys"] is not None

    def test_decoder_phys_ok_input_path(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_phys*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            decoded_image = PNGCodec.decode(Path(good_image_path))

            assert decoded_image["phys"] is not None

    def test_decoder_phys_ok_input_file(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_phys*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            with open(good_image_path, "rb") as pngfile:
                decoded_image = PNGCodec.decode(pngfile)

                assert decoded_image["phys"] is not None

    def test_decoder_phys_ok_input_bytes(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_phys*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            with open(good_image_path, "rb") as pngfile:
                decoded_image = PNGCodec.decode(pngfile.read())

                assert decoded_image["phys"] is not None

    def test_decoder_phys_bad_input_str(self):
        BAD_IMAGES_PATHS = glob.glob("./tests/testimages/bad_phys*.png")
        for bad_image_path in BAD_IMAGES_PATHS:
            decoded_image = PNGCodec.decode(bad_image_path)

            assert decoded_image["phys"] is not None
            assert decoded_image["phys"]["unit"] == "aspect_ratio"

    def test_decoder_phys_bad_input_path(self):
        BAD_IMAGES_PATHS = glob.glob("./tests/testimages/bad_phys*.png")
        for bad_image_path in BAD_IMAGES_PATHS:
            decoded_image = PNGCodec.decode(Path(bad_image_path))

            assert decoded_image["phys"] is not None
            assert decoded_image["phys"]["unit"] == "aspect_ratio"

    def test_decoder_phys_bad_input_file(self):
        BAD_IMAGES_PATHS = glob.glob("./tests/testimages/bad_phys*.png")
        for bad_image_path in BAD_IMAGES_PATHS:
            with open(bad_image_path, "rb") as pngfile:
                decoded_image = PNGCodec.decode(pngfile)

                assert decoded_image["phys"] is not None
                assert decoded_image["phys"]["unit"] == "aspect_ratio"

    def test_decoder_phys_bad_input_bytes(self):
        BAD_IMAGES_PATHS = glob.glob("./tests/testimages/bad_phys*.png")
        for bad_image_path in BAD_IMAGES_PATHS:
            with open(bad_image_path, "rb") as pngfile:
                decoded_image = PNGCodec.decode(pngfile.read())

                assert decoded_image["phys"] is not None
                assert decoded_image["phys"]["unit"] == "aspect_ratio"

    def test_decoder_gama_ok_input_str(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_gama*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            decoded_image = PNGCodec.decode(good_image_path)

            assert decoded_image["gama"] is not None

    def test_decoder_gama_ok_input_path(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_gama*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            decoded_image = PNGCodec.decode(Path(good_image_path))

            assert decoded_image["gama"] is not None

    def test_decoder_gama_ok_input_file(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_gama*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            with open(good_image_path, "rb") as pngfile:
                decoded_image = PNGCodec.decode(pngfile)

                assert decoded_image["gama"] is not None

    def test_decoder_gama_ok_input_bytes(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_gama*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            with open(good_image_path, "rb") as pngfile:
                decoded_image = PNGCodec.decode(pngfile.read())

                assert decoded_image["gama"] is not None

    def test_decoder_gama_bad_input_str(self):
        BAD_IMAGES_PATHS = glob.glob("./tests/testimages/bad_gama*.png")
        for bad_image_path in BAD_IMAGES_PATHS:
            decoded_image = PNGCodec.decode(bad_image_path)

            assert decoded_image["gama"] is None

    def test_decoder_gama_bad_input_path(self):
        BAD_IMAGES_PATHS = glob.glob("./tests/testimages/bad_gama*.png")
        for bad_image_path in BAD_IMAGES_PATHS:
            decoded_image = PNGCodec.decode(Path(bad_image_path))

            assert decoded_image["gama"] is None

    def test_decoder_gama_bad_input_file(self):
        BAD_IMAGES_PATHS = glob.glob("./tests/testimages/bad_gama*.png")
        for bad_image_path in BAD_IMAGES_PATHS:
            with open(bad_image_path, "rb") as pngfile:
                decoded_image = PNGCodec.decode(pngfile)

                assert decoded_image["gama"] is None

    def test_decoder_gama_bad_input_bytes(self):
        BAD_IMAGES_PATHS = glob.glob("./tests/testimages/bad_gama*.png")
        for bad_image_path in BAD_IMAGES_PATHS:
            with open(bad_image_path, "rb") as pngfile:
                decoded_image = PNGCodec.decode(pngfile.read())

                assert decoded_image["gama"] is None

    def test_decoder_chrm_ok_input_str(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_chrm*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            decoded_image = PNGCodec.decode(good_image_path)

            assert decoded_image["chrm"] is not None
            assert len(decoded_image["chrm"]) == 8

    def test_decoder_chrm_ok_input_path(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_chrm*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            decoded_image = PNGCodec.decode(Path(good_image_path))

            assert decoded_image["chrm"] is not None
            assert len(decoded_image["chrm"]) == 8

    def test_decoder_chrm_ok_input_file(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_chrm*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            with open(good_image_path, "rb") as pngfile:
                decoded_image = PNGCodec.decode(pngfile)

                assert decoded_image["chrm"] is not None
                assert len(decoded_image["chrm"]) == 8

    def test_decoder_chrm_ok_input_bytes(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_chrm*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            with open(good_image_path, "rb") as pngfile:
                decoded_image = PNGCodec.decode(pngfile.read())

                assert decoded_image["chrm"] is not None
                assert len(decoded_image["chrm"]) == 8

    def test_decoder_chrm_bad_input_str(self):
        BAD_IMAGES_PATHS = glob.glob("./tests/testimages/bad_chrm*.png")
        for bad_image_path in BAD_IMAGES_PATHS:
            decoded_image = PNGCodec.decode(bad_image_path)

            assert decoded_image["chrm"] is None

    def test_decoder_chrm_bad_input_path(self):
        BAD_IMAGES_PATHS = glob.glob("./tests/testimages/bad_chrm*.png")
        for bad_image_path in BAD_IMAGES_PATHS:
            decoded_image = PNGCodec.decode(Path(bad_image_path))

            assert decoded_image["chrm"] is None

    def test_decoder_chrm_bad_input_file(self):
        BAD_IMAGES_PATHS = glob.glob("./tests/testimages/bad_chrm*.png")
        for bad_image_path in BAD_IMAGES_PATHS:
            with open(bad_image_path, "rb") as pngfile:
                decoded_image = PNGCodec.decode(pngfile)

                assert decoded_image["chrm"] is None

    def test_decoder_chrm_bad_input_bytes(self):
        BAD_IMAGES_PATHS = glob.glob("./tests/testimages/bad_chrm*.png")
        for bad_image_path in BAD_IMAGES_PATHS:
            with open(bad_image_path, "rb") as pngfile:
                decoded_image = PNGCodec.decode(pngfile.read())

                assert decoded_image["chrm"] is None

    def test_decoder_sbit_ok_input_str(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_sbit*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            decoded_image = PNGCodec.decode(good_image_path)

            assert decoded_image["sbit"] is not None

    def test_decoder_sbit_ok_input_path(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_sbit*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            decoded_image = PNGCodec.decode(Path(good_image_path))

            assert decoded_image["sbit"] is not None

    def test_decoder_sbit_ok_input_file(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_sbit*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            with open(good_image_path, "rb") as pngfile:
                decoded_image = PNGCodec.decode(pngfile)

                assert decoded_image["sbit"] is not None

    def test_decoder_sbit_ok_input_bytes(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_sbit*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            with open(good_image_path, "rb") as pngfile:
                decoded_image = PNGCodec.decode(pngfile.read())

                assert decoded_image["sbit"] is not None

    def test_decoder_sbit_bad_input_str(self):
        BAD_IMAGES_PATHS = glob.glob("./tests/testimages/bad_sbit*.png")
        for bad_image_path in BAD_IMAGES_PATHS:
            decoded_image = PNGCodec.decode(bad_image_path)

            assert decoded_image["sbit"] is None

    def test_decoder_sbit_bad_input_path(self):
        BAD_IMAGES_PATHS = glob.glob("./tests/testimages/bad_sbit*.png")
        for bad_image_path in BAD_IMAGES_PATHS:
            decoded_image = PNGCodec.decode(Path(bad_image_path))

            assert decoded_image["sbit"] is None

    def test_decoder_sbit_bad_input_file(self):
        BAD_IMAGES_PATHS = glob.glob("./tests/testimages/bad_sbit*.png")
        for bad_image_path in BAD_IMAGES_PATHS:
            with open(bad_image_path, "rb") as pngfile:
                decoded_image = PNGCodec.decode(pngfile)

                assert decoded_image["sbit"] is None

    def test_decoder_sbit_bad_input_bytes(self):
        BAD_IMAGES_PATHS = glob.glob("./tests/testimages/bad_sbit*.png")
        for bad_image_path in BAD_IMAGES_PATHS:
            with open(bad_image_path, "rb") as pngfile:
                decoded_image = PNGCodec.decode(pngfile.read())

                assert decoded_image["sbit"] is None

    def test_decoder_srgb_ok_input_str(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_srgb*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            decoded_image = PNGCodec.decode(good_image_path)

            assert decoded_image["srgb"] is not None

    def test_decoder_srgb_ok_input_path(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_srgb*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            decoded_image = PNGCodec.decode(Path(good_image_path))

            assert decoded_image["srgb"] is not None

    def test_decoder_srgb_ok_input_file(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_srgb*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            with open(good_image_path, "rb") as pngfile:
                decoded_image = PNGCodec.decode(pngfile)

                assert decoded_image["srgb"] is not None

    def test_decoder_srgb_ok_input_bytes(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_srgb*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            with open(good_image_path, "rb") as pngfile:
                decoded_image = PNGCodec.decode(pngfile.read())

                assert decoded_image["srgb"] is not None

    def test_decoder_srgb_bad_input_str(self):
        BAD_IMAGES_PATHS = glob.glob("./tests/testimages/bad_srgb*.png")
        for bad_image_path in BAD_IMAGES_PATHS:
            decoded_image = PNGCodec.decode(bad_image_path)

            assert decoded_image["srgb"] is None

    def test_decoder_srgb_bad_input_path(self):
        BAD_IMAGES_PATHS = glob.glob("./tests/testimages/bad_srgb*.png")
        for bad_image_path in BAD_IMAGES_PATHS:
            decoded_image = PNGCodec.decode(Path(bad_image_path))

            assert decoded_image["srgb"] is None

    def test_decoder_srgb_bad_input_file(self):
        BAD_IMAGES_PATHS = glob.glob("./tests/testimages/bad_srgb*.png")
        for bad_image_path in BAD_IMAGES_PATHS:
            with open(bad_image_path, "rb") as pngfile:
                decoded_image = PNGCodec.decode(pngfile)

                assert decoded_image["srgb"] is None

    def test_decoder_srgb_bad_input_bytes(self):
        BAD_IMAGES_PATHS = glob.glob("./tests/testimages/bad_srgb*.png")
        for bad_image_path in BAD_IMAGES_PATHS:
            with open(bad_image_path, "rb") as pngfile:
                decoded_image = PNGCodec.decode(pngfile.read())

                assert decoded_image["srgb"] is None

    def test_decoder_bkgd_ok_input_str(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_bkgd*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            decoded_image = PNGCodec.decode(good_image_path)

            if decoded_image['color_type'] in [0, 4]:
                assert decoded_image["bkgd"] is not None
                assert len(decoded_image["bkgd"]) == 1
            elif decoded_image['color_type'] in [2, 6]:
                assert decoded_image["bkgd"] is not None
                assert len(decoded_image["bkgd"]) == 3
            elif decoded_image['color_type'] in [3]:
                assert decoded_image["bkgd"] is not None

    def test_decoder_bkgd_ok_input_path(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_bkgd*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            decoded_image = PNGCodec.decode(Path(good_image_path))

            if decoded_image['color_type'] in [0, 4]:
                assert decoded_image["bkgd"] is not None
                assert len(decoded_image["bkgd"]) == 1
            elif decoded_image['color_type'] in [2, 6]:
                assert decoded_image["bkgd"] is not None
                assert len(decoded_image["bkgd"]) == 3
            elif decoded_image['color_type'] in [3]:
                assert decoded_image["bkgd"] is not None

    def test_decoder_bkgd_ok_input_file(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_bkgd*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            with open(good_image_path, "rb") as pngfile:
                decoded_image = PNGCodec.decode(pngfile)

                if decoded_image['color_type'] in [0, 4]:
                    assert decoded_image["bkgd"] is not None
                    assert len(decoded_image["bkgd"]) == 1
                elif decoded_image['color_type'] in [2, 6]:
                    assert decoded_image["bkgd"] is not None
                    assert len(decoded_image["bkgd"]) == 3
                elif decoded_image['color_type'] in [3]:
                    assert decoded_image["bkgd"] is not None

    def test_decoder_bkgd_ok_input_bytes(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_bkgd*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            with open(good_image_path, "rb") as pngfile:
                decoded_image = PNGCodec.decode(pngfile.read())

                if decoded_image['color_type'] in [0, 4]:
                    assert decoded_image["bkgd"] is not None
                    assert len(decoded_image["bkgd"]) == 1
                elif decoded_image['color_type'] in [2, 6]:
                    assert decoded_image["bkgd"] is not None
                    assert len(decoded_image["bkgd"]) == 3
                elif decoded_image['color_type'] in [3]:
                    assert decoded_image["bkgd"] is not None

    def test_decoder_bkgd_bad_input_str(self):
        BAD_IMAGES_PATHS = glob.glob("./tests/testimages/bad_bkgd*.png")
        for bad_image_path in BAD_IMAGES_PATHS:
            decoded_image = PNGCodec.decode(bad_image_path)

            assert decoded_image["bkgd"] is None

    def test_decoder_bkgd_bad_input_path(self):
        BAD_IMAGES_PATHS = glob.glob("./tests/testimages/bad_bkgd*.png")
        for bad_image_path in BAD_IMAGES_PATHS:
            decoded_image = PNGCodec.decode(Path(bad_image_path))

            assert decoded_image["bkgd"] is None

    def test_decoder_bkgd_bad_input_file(self):
        BAD_IMAGES_PATHS = glob.glob("./tests/testimages/bad_bkgd*.png")
        for bad_image_path in BAD_IMAGES_PATHS:
            with open(bad_image_path, "rb") as pngfile:
                decoded_image = PNGCodec.decode(pngfile)

                assert decoded_image["bkgd"] is None

    def test_decoder_bkgd_bad_input_bytes(self):
        BAD_IMAGES_PATHS = glob.glob("./tests/testimages/bad_bkgd*.png")
        for bad_image_path in BAD_IMAGES_PATHS:
            with open(bad_image_path, "rb") as pngfile:
                decoded_image = PNGCodec.decode(pngfile.read())

                assert decoded_image["bkgd"] is None

    def test_decoder_hist_ok_input_str(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_hist*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            decoded_image = PNGCodec.decode(good_image_path)

            assert decoded_image['histogram'] is not None
            assert len(decoded_image['histogram']) == len(decoded_image['palette'])

    def test_decoder_hist_ok_input_path(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_hist*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            decoded_image = PNGCodec.decode(Path(good_image_path))

            assert decoded_image['histogram'] is not None
            assert len(decoded_image['histogram']) == len(decoded_image['palette'])

    def test_decoder_hist_ok_input_file(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_hist*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            with open(good_image_path, "rb") as pngfile:
                decoded_image = PNGCodec.decode(pngfile)

                assert decoded_image['histogram'] is not None
                assert len(decoded_image['histogram']) == len(decoded_image['palette'])

    def test_decoder_hist_ok_input_bytes(self):
        GOOD_IMAGES_PATHS = glob.glob("./tests/testimages/good_hist*.png")
        for good_image_path in GOOD_IMAGES_PATHS:
            with open(good_image_path, "rb") as pngfile:
                decoded_image = PNGCodec.decode(pngfile.read())

                assert decoded_image['histogram'] is not None
                assert len(decoded_image['histogram']) == len(decoded_image['palette'])

    def test_decoder_hist_bad_input_str(self):
        BAD_IMAGES_PATHS = glob.glob("./tests/testimages/bad_hist*.png")
        for bad_image_path in BAD_IMAGES_PATHS:
            decoded_image = PNGCodec.decode(bad_image_path)

            assert decoded_image['histogram'] is None

    def test_decoder_hist_bad_input_path(self):
        BAD_IMAGES_PATHS = glob.glob("./tests/testimages/bad_hist*.png")
        for bad_image_path in BAD_IMAGES_PATHS:
            decoded_image = PNGCodec.decode(Path(bad_image_path))

            assert decoded_image['histogram'] is None

    def test_decoder_hist_bad_input_file(self):
        BAD_IMAGES_PATHS = glob.glob("./tests/testimages/bad_hist*.png")
        for bad_image_path in BAD_IMAGES_PATHS:
            with open(bad_image_path, "rb") as pngfile:
                decoded_image = PNGCodec.decode(pngfile)

                assert decoded_image['histogram'] is None

    def test_decoder_hist_bad_input_bytes(self):
        BAD_IMAGES_PATHS = glob.glob("./tests/testimages/bad_hist*.png")
        for bad_image_path in BAD_IMAGES_PATHS:
            with open(bad_image_path, "rb") as pngfile:
                decoded_image = PNGCodec.decode(pngfile.read())

                assert decoded_image['histogram'] is None