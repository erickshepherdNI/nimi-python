

include $(BUILD_HELPER_DIR)/defines.mak

MODULE_FILES_TO_GENERATE := $(DEFAULT_PY_FILES_TO_GENERATE)

MODULE_FILES_TO_COPY := $(DEFAULT_PY_FILES_TO_COPY)

RST_FILES_TO_GENERATE := $(DEFAULT_RST_FILES_TO_GENERATE)

CUSTOM_TYPES_TO_COPY += \
    waveform_info.py \
    ni_complex_number.py \
    spectrum_info_t.py \

include $(BUILD_HELPER_DIR)/rules.mak

