from pathlib import Path

import pytest

from vpypng import PNGCodec, PNGImage


class TestPngCodecDecode:
    def test_codec_exists(self):
        assert PNGCodec is not None
        assert PNGCodec.decode is not None

    def test_codec_input_is_string_correct(self):
        correct_image_absolute_path = "/mnt/d/vpypng/tests/testimages/good_ztxt.png"
        decoded_image = PNGCodec.decode(correct_image_absolute_path)
        assert decoded_image is not None
        assert isinstance(decoded_image, PNGImage)

    def test_codec_input_is_string_correct_relative(self):
        correct_image_relative_path = "tests/testimages/good_ztxt.png"
        decoded_image = PNGCodec.decode(correct_image_relative_path)
        assert decoded_image is not None
        assert isinstance(decoded_image, PNGImage)

    def test_codec_input_is_string_incorrect(self):
        incorrect_image_absolute_path = "/mnt/d/vpypng/tests/testimages/incorrect.png"
        with pytest.raises(FileNotFoundError):
            PNGCodec.decode(incorrect_image_absolute_path)

    def test_codec_input_is_string_incorrect_relative(self):
        incorrect_image_relative_path = "tests/testimages/incorrect.png"
        with pytest.raises(FileNotFoundError):
            PNGCodec.decode(incorrect_image_relative_path)

    def test_codec_input_is_path_correct(self):
        correct_image_absolute_path = "/mnt/d/vpypng/tests/testimages/good_ztxt.png"
        decoded_image = PNGCodec.decode(Path(correct_image_absolute_path))
        assert decoded_image is not None
        assert isinstance(decoded_image, PNGImage)

    def test_codec_input_is_path_correct_relative(self):
        correct_image_relative_path = "tests/testimages/good_ztxt.png"
        decoded_image = PNGCodec.decode(Path(correct_image_relative_path))
        assert decoded_image is not None
        assert isinstance(decoded_image, PNGImage)

    def test_codec_input_is_path_incorrect(self):
        incorrect_image_absolute_path = "/mnt/d/vpypng/tests/testimages/incorrect.png"
        with pytest.raises(FileNotFoundError):
            PNGCodec.decode(Path(incorrect_image_absolute_path))

    def test_codec_input_is_path_incorrect_relative(self):
        incorrect_image_relative_path = "tests/testimages/incorrect.png"
        with pytest.raises(FileNotFoundError):
            PNGCodec.decode(Path(incorrect_image_relative_path))

    def test_codec_input_is_file_correct(self):
        correct_image_absolute_path = "/mnt/d/vpypng/tests/testimages/good_ztxt.png"
        with open(correct_image_absolute_path, "rb") as pngfile:
            decoded_image = PNGCodec.decode(pngfile)
            assert decoded_image is not None
            assert isinstance(decoded_image, PNGImage)

    def test_codec_input_is_file_correct_relative(self):
        correct_image_relative_path = "tests/testimages/good_ztxt.png"
        with open(correct_image_relative_path, "rb") as pngfile:
            decoded_image = PNGCodec.decode(pngfile)
            assert decoded_image is not None
            assert isinstance(decoded_image, PNGImage)

    def test_codec_input_is_bytes_correct(self):
        correct_image_absolute_path = "/mnt/d/vpypng/tests/testimages/good_ztxt.png"
        with open(correct_image_absolute_path, "rb") as pngfile:
            decoded_image = PNGCodec.decode(pngfile.read())
            assert decoded_image is not None
            assert isinstance(decoded_image, PNGImage)
