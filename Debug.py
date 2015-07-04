# File has up to ten debug levels.  High debug = low number

# SETS THE CURRENT DEBUG LEVEL
DEBUG_LEVEL = 10

# DEBUG LEVELS
DEBUG_LEVEL_HIGH = 1
DEBUG_LEVEL_MEDIUM = 5
DEBUG_LEVEL_LOW = 10

# Debug Function
# Call with printable object and integer level
def debug(message, debug_level):
    if debug_level <= DEBUG_LEVEL:
        print message
