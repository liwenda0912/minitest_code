# 使用driver.press_keycode(number)
#
# 其中number为数字，代表不同按键，具体如下：
#
# keycode
# 4：返回键(Back
# key)
#
# keycode
# 5：电话键(Call
# key)
#
# keycode
# 6：结束通话键(End
# Call
# key)
#
# keycode
# 7 - 16：依次为数字0 - 9
#
# keycode
# 17： *
#
# keycode
# 18：  #
#
# keycode
# 19 - 23：上、下、左、右、中间
#
# keycode
# 24 - 25：音量上、下
#
# keycode
# 26：电源键(Power
# key)
#
# keycode
# 27：相机键(Camera
# key)
#
# keycode
# 28：清除键(Clear
# key)
#
# keycode
# 29 - 54：字母A - Z
#
# keycode
# 55：,
#
# keycode
# 56：.
#
# keycode
# 61：Tab键(Tab
# key)
#
# keycode
# 62：空格键(Space
# key)
#
# keycode
# 66：回车键(Enter
# key)
#
# keycode
# 67：退格键(Backspace
# key)
#
# keycode
# 68：`
#
# keycode
# 69：-
#
# keycode
# 70：=
#
# keycode
# 71：[
#
# keycode 72：]
#
# keycode
# 73： \
#  \
#     keycode
# 74：;
#
# keycode
# 75：'
#
# keycode
# 76： /
#
# keycode
# 77：
#
# @
#
#
# keycode
# 81：+
#
# keycode
# 82：菜单键(Menu
# key)
#
# keycode
# 84：搜索键(Search
# key)
#
# keycode
# 164：静音键(Volume
# Mute
# key)
#
#
#
# keycode
# 7 - 16：依次为数字0 - 9，所以使用时可以自定义一个字典，譬如这里需要输入的是手机号, 定义一个num字典，其中key为数字，value为对应的按键

class ke_code:
    @staticmethod
    def get_keys():
        key = {'0': 7, '1': 8, '2': 9, '3': 10, '4': 11, '5': 12, '6': 13, '7': 14, '8': 15, '9': 16,
               'A': 29, 'B': 30, 'C': 31, 'D': 32, 'E': 33, 'F': 34, 'G': 35, 'H': 36, 'I': 37, 'J': 38,
               'K': 39, 'L': 40, 'M': 41, 'N': 42, 'O': 43, 'P': 44, 'Q': 45, 'R': 46, 'S': 47, 'T': 48,
               'U': 49, 'V': 50, 'W': 51, 'X': 52, 'Y': 53, 'Z': 54,
               'a': 29, 'b': 30, 'c': 31, 'd': 32, 'e': 33, 'f': 34, 'g': 35, 'h': 36, 'i': 37, 'j': 38,
               'k': 39, 'l': 40, 'm': 41, 'n': 42, 'o': 43, 'p': 44, 'q': 45, 'r': 46, 's': 47, 't': 48,
               'u': 49, 'v': 50, 'w': 51, 'x': 52, 'y': 53, 'z': 54,
               'META_ALT_LEFT_ON': 16,
               'META_ALT_MASK': 50,
               'META_ALT_ON': 2,
               'META_ALT_RIGHT_ON': 32,
               'META_CAPS_LOCK_ON': 1048576,
               'META_CTRL_LEFT_ON': 8192,
               'META_CTRL_MASK': 28672,
               'META_CTRL_ON': 4096,
               'META_CTRL_RIGHT_ON': 16384,
               'META_FUNCTION_ON': 8,
               'META_META_LEFT_ON': 131072,
               'META_META_MASK': 458752,
               'META_META_ON': 65536,
               'META_META_RIGHT_ON': 262144,
               'META_NUM_LOCK_ON': 2097152,
               'META_SCROLL_LOCK_ON': 4194304,
               'META_SHIFT_LEFT_ON': 64,
               'META_SHIFT_MASK': 193,
               'META_SHIFT_ON': 1,
               'META_SHIFT_RIGHT_ON': 128,
               'META_SYM_ON': 4,
               'KEYCODE_APOSTROPHE': 75,
               'KEYCODE_AT': 77,
               'KEYCODE_BACKSLASH': 73,
               'KEYCODE_COMMA': 55,
               'KEYCODE_EQUALS': 70,
               'KEYCODE_GRAVE': 68,
               'KEYCODE_LEFT_BRACKET': 71,
               'KEYCODE_MINUS': 69,
               'KEYCODE_PERIOD': 56,
               'KEYCODE_PLUS': 81,
               'KEYCODE_POUND': 18,
               'KEYCODE_RIGHT_BRACKET': 72,
               'KEYCODE_SEMICOLON': 74,
               'KEYCODE_SLASH': 76,
               'KEYCODE_STAR': 17,
               'KEYCODE_SPACE': 62,
               'KEYCODE_TAB': 61,
               'KEYCODE_ENTER': 66,
               'KEYCODE_ESCAPE': 111,
               'KEYCODE_CAPS_LOCK': 115,
               'KEYCODE_CLEAR': 28,
               'KEYCODE_PAGE_DOWN': 93,
               'KEYCODE_PAGE_UP': 92,
               'KEYCODE_SCROLL_LOCK': 116,
               'KEYCODE_MOVE_END': 123,
               'KEYCODE_MOVE_HOME': 122,
               'KEYCODE_INSERT': 124,
               'KEYCODE_SHIFT_LEFT': 59,
               'KEYCODE_SHIFT_RIGHT': 60,
               'KEYCODE_F1': 131,
               'KEYCODE_F2': 132,
               'KEYCODE_F3': 133,
               'KEYCODE_F4': 134,
               'KEYCODE_F5': 135,
               'KEYCODE_F6': 136,
               'KEYCODE_F7': 137,
               'KEYCODE_F8': 138,
               'KEYCODE_F9': 139,
               'KEYCODE_F10': 140,
               'KEYCODE_F11': 141,
               'KEYCODE_F12': 142,
               'KEYCODE_BACK': 4,
               'KEYCODE_CALL': 5,
               'KEYCODE_ENDCALL': 6,
               'KEYCODE_CAMERA': 27,
               'KEYCODE_FOCUS': 80,
               'KEYCODE_VOLUME_UP': 24,
               'KEYCODE_VOLUME_DOWN': 25,
               'KEYCODE_VOLUME_MUTE': 164,
               'KEYCODE_MENU': 82,
               'KEYCODE_HOME': 3,
               'KEYCODE_POWER': 26,
               'KEYCODE_SEARCH': 84,
               'KEYCODE_NOTIFICATION': 83,
               'KEYCODE_NUM': 78,
               'KEYCODE_SYM': 63,
               'KEYCODE_SETTINGS': 176,
               'KEYCODE_DEL': 67,
               'KEYCODE_FORWARD_DEL': 112,
               'KEYCODE_NUMPAD_0': 144,
               'KEYCODE_NUMPAD_1': 145,
               'KEYCODE_NUMPAD_2': 146,
               'KEYCODE_NUMPAD_3': 147,
               'KEYCODE_NUMPAD_4': 148,
               'KEYCODE_NUMPAD_5': 149,
               'KEYCODE_NUMPAD_6': 150,
               'KEYCODE_NUMPAD_7': 151,
               'KEYCODE_NUMPAD_8': 152,
               'KEYCODE_NUMPAD_9': 153,
               'KEYCODE_NUMPAD_ADD': 157,
               'KEYCODE_NUMPAD_COMMA': 159,
               'KEYCODE_NUMPAD_DIVIDE': 154,
               'KEYCODE_NUMPAD_DOT': 158,
               'KEYCODE_NUMPAD_EQUALS': 161,
               'KEYCODE_NUMPAD_LEFT_PAREN': 162,
               'KEYCODE_NUMPAD_MULTIPLY': 155,
               'KEYCODE_NUMPAD_RIGHT_PAREN': 163,
               'KEYCODE_NUMPAD_SUBTRACT': 156,
               'KEYCODE_NUMPAD_ENTER': 160,
               'KEYCODE_NUM_LOCK': 143,
               'KEYCODE_MEDIA_FAST_FORWARD': 90,
               'KEYCODE_MEDIA_NEXT': 87,
               'KEYCODE_MEDIA_PAUSE': 127,
               'KEYCODE_MEDIA_PLAY': 126,
               'KEYCODE_MEDIA_PLAY_PAUSE': 85,
               'KEYCODE_MEDIA_PREVIOUS': 88,
               'KEYCODE_MEDIA_RECORD': 130,
               'KEYCODE_MEDIA_REWIND': 89,
               'KEYCODE_MEDIA_STOP': 86,
               '.': 56
               }
        return key
# 使用driver.press_keycode(number)
#
# 其中number为数字，代表不同按键，具体如下：
#
# keycode
# 4：返回键(Back
# key)
#
# keycode
# 5：电话键(Call
# key)
#
# keycode
# 6：结束通话键(End
# Call
# key)
#
# keycode
# 7 - 16：依次为数字0 - 9
#
# keycode
# 17： *
#
# keycode
# 18：  #
#
# keycode
# 19 - 23：上、下、左、右、中间
#
# keycode
# 24 - 25：音量上、下
#
# keycode
# 26：电源键(Power
# key)
#
# keycode
# 27：相机键(Camera
# key)
#
# keycode
# 28：清除键(Clear
# key)
#
# keycode
# 29 - 54：字母A - Z
#
# keycode
# 55：,
#
# keycode
# 56：.
#
# keycode
# 61：Tab键(Tab
# key)
#
# keycode
# 62：空格键(Space
# key)
#
# keycode
# 66：回车键(Enter
# key)
#
# keycode
# 67：退格键(Backspace
# key)
#
# keycode
# 68：`
#
# keycode
# 69：-
#
# keycode
# 70：=
#
# keycode
# 71：[
#
# keycode 72：]
#
# keycode
# 73： \
#  \
#     keycode
# 74：;
#
# keycode
# 75：'
#
# keycode
# 76： /
#
# keycode
# 77：
#
# @
#
#
# keycode
# 81：+
#
# keycode
# 82：菜单键(Menu
# key)
#
# keycode
# 84：搜索键(Search
# key)
#
# keycode
# 164：静音键(Volume
# Mute
# key)
#
#
#
# keycode
# 7 - 16：依次为数字0 - 9，所以使用时可以自定义一个字典，譬如这里需要输入的是手机号, 定义一个num字典，其中key为数字，value为对应的按键

class ke_code:
    @staticmethod
    def get_keys():
        key = {'0': 7, '1': 8, '2': 9, '3': 10, '4': 11, '5': 12, '6': 13, '7': 14, '8': 15, '9': 16,
               'A': 29, 'B': 30, 'C': 31, 'D': 32, 'E': 33, 'F': 34, 'G': 35, 'H': 36, 'I': 37, 'J': 38,
               'K': 39, 'L': 40, 'M': 41, 'N': 42, 'O': 43, 'P': 44, 'Q': 45, 'R': 46, 'S': 47, 'T': 48,
               'U': 49, 'V': 50, 'W': 51, 'X': 52, 'Y': 53, 'Z': 54,
               'a': 29, 'b': 30, 'c': 31, 'd': 32, 'e': 33, 'f': 34, 'g': 35, 'h': 36, 'i': 37, 'j': 38,
               'k': 39, 'l': 40, 'm': 41, 'n': 42, 'o': 43, 'p': 44, 'q': 45, 'r': 46, 's': 47, 't': 48,
               'u': 49, 'v': 50, 'w': 51, 'x': 52, 'y': 53, 'z': 54,
               'META_ALT_LEFT_ON': 16,
               'META_ALT_MASK': 50,
               'META_ALT_ON': 2,
               'META_ALT_RIGHT_ON': 32,
               'META_CAPS_LOCK_ON': 1048576,
               'META_CTRL_LEFT_ON': 8192,
               'META_CTRL_MASK': 28672,
               'META_CTRL_ON': 4096,
               'META_CTRL_RIGHT_ON': 16384,
               'META_FUNCTION_ON': 8,
               'META_META_LEFT_ON': 131072,
               'META_META_MASK': 458752,
               'META_META_ON': 65536,
               'META_META_RIGHT_ON': 262144,
               'META_NUM_LOCK_ON': 2097152,
               'META_SCROLL_LOCK_ON': 4194304,
               'META_SHIFT_LEFT_ON': 64,
               'META_SHIFT_MASK': 193,
               'META_SHIFT_ON': 1,
               'META_SHIFT_RIGHT_ON': 128,
               'META_SYM_ON': 4,
               'KEYCODE_APOSTROPHE': 75,
               'KEYCODE_AT': 77,
               'KEYCODE_BACKSLASH': 73,
               'KEYCODE_COMMA': 55,
               'KEYCODE_EQUALS': 70,
               'KEYCODE_GRAVE': 68,
               'KEYCODE_LEFT_BRACKET': 71,
               'KEYCODE_MINUS': 69,
               'KEYCODE_PERIOD': 56,
               'KEYCODE_PLUS': 81,
               'KEYCODE_POUND': 18,
               'KEYCODE_RIGHT_BRACKET': 72,
               'KEYCODE_SEMICOLON': 74,
               'KEYCODE_SLASH': 76,
               'KEYCODE_STAR': 17,
               'KEYCODE_SPACE': 62,
               'KEYCODE_TAB': 61,
               'KEYCODE_ENTER': 66,
               'KEYCODE_ESCAPE': 111,
               'KEYCODE_CAPS_LOCK': 115,
               'KEYCODE_CLEAR': 28,
               'KEYCODE_PAGE_DOWN': 93,
               'KEYCODE_PAGE_UP': 92,
               'KEYCODE_SCROLL_LOCK': 116,
               'KEYCODE_MOVE_END': 123,
               'KEYCODE_MOVE_HOME': 122,
               'KEYCODE_INSERT': 124,
               'KEYCODE_SHIFT_LEFT': 59,
               'KEYCODE_SHIFT_RIGHT': 60,
               'KEYCODE_F1': 131,
               'KEYCODE_F2': 132,
               'KEYCODE_F3': 133,
               'KEYCODE_F4': 134,
               'KEYCODE_F5': 135,
               'KEYCODE_F6': 136,
               'KEYCODE_F7': 137,
               'KEYCODE_F8': 138,
               'KEYCODE_F9': 139,
               'KEYCODE_F10': 140,
               'KEYCODE_F11': 141,
               'KEYCODE_F12': 142,
               'KEYCODE_BACK': 4,
               'KEYCODE_CALL': 5,
               'KEYCODE_ENDCALL': 6,
               'KEYCODE_CAMERA': 27,
               'KEYCODE_FOCUS': 80,
               'KEYCODE_VOLUME_UP': 24,
               'KEYCODE_VOLUME_DOWN': 25,
               'KEYCODE_VOLUME_MUTE': 164,
               'KEYCODE_MENU': 82,
               'KEYCODE_HOME': 3,
               'KEYCODE_POWER': 26,
               'KEYCODE_SEARCH': 84,
               'KEYCODE_NOTIFICATION': 83,
               'KEYCODE_NUM': 78,
               'KEYCODE_SYM': 63,
               'KEYCODE_SETTINGS': 176,
               'KEYCODE_DEL': 67,
               'KEYCODE_FORWARD_DEL': 112,
               'KEYCODE_NUMPAD_0': 144,
               'KEYCODE_NUMPAD_1': 145,
               'KEYCODE_NUMPAD_2': 146,
               'KEYCODE_NUMPAD_3': 147,
               'KEYCODE_NUMPAD_4': 148,
               'KEYCODE_NUMPAD_5': 149,
               'KEYCODE_NUMPAD_6': 150,
               'KEYCODE_NUMPAD_7': 151,
               'KEYCODE_NUMPAD_8': 152,
               'KEYCODE_NUMPAD_9': 153,
               'KEYCODE_NUMPAD_ADD': 157,
               'KEYCODE_NUMPAD_COMMA': 159,
               'KEYCODE_NUMPAD_DIVIDE': 154,
               'KEYCODE_NUMPAD_DOT': 158,
               'KEYCODE_NUMPAD_EQUALS': 161,
               'KEYCODE_NUMPAD_LEFT_PAREN': 162,
               'KEYCODE_NUMPAD_MULTIPLY': 155,
               'KEYCODE_NUMPAD_RIGHT_PAREN': 163,
               'KEYCODE_NUMPAD_SUBTRACT': 156,
               'KEYCODE_NUMPAD_ENTER': 160,
               'KEYCODE_NUM_LOCK': 143,
               'KEYCODE_MEDIA_FAST_FORWARD': 90,
               'KEYCODE_MEDIA_NEXT': 87,
               'KEYCODE_MEDIA_PAUSE': 127,
               'KEYCODE_MEDIA_PLAY': 126,
               'KEYCODE_MEDIA_PLAY_PAUSE': 85,
               'KEYCODE_MEDIA_PREVIOUS': 88,
               'KEYCODE_MEDIA_RECORD': 130,
               'KEYCODE_MEDIA_REWIND': 89,
               'KEYCODE_MEDIA_STOP': 86,
               '.': 56
               }
        return key
