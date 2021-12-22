import telebot
import values

class CurrentState(telebot.AdvancedCustomFilter):
    key = 'current_state'
    @staticmethod
    def check(message, current_state):
        return values.current_state in current_state
        