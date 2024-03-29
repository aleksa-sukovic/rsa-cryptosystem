from Prompts.BasePrompt import BasePrompt
from Validators.NumberValidator import NumberValidator

class PrimeGeneratorPrompt(BasePrompt):
    def __init__(self):
        super(PrimeGeneratorPrompt, self).__init__(({
            'type': 'input',
            'name': 'length',
            'message': 'Duzina broja (u bitima):',
            'validate': NumberValidator
        }, {
            'type': 'input',
            'name': 'count',
            'message': 'Koliko brojeva zelite generisati?',
            'validate': NumberValidator
        }))
    
    def hasRequiredAnswers(self, answers):
        hasRequired = True
        hasRequired = hasRequired and 'length' in answers
        hasRequired = hasRequired and 'count' in answers
        return hasRequired