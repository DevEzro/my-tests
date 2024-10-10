import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import random

class ComplexAgent:
    def __init__(self):
        self.responses = {
            "saludos": ["¡Hola! ¿Cómo puedo ayudarte hoy?", "¡Buenas! ¿En qué puedo ayudarte?"],
            "despedidas": ["¡Hasta luego! Que tengas un buen día.", "Adiós, ¡cuídate!"],
            "preguntas": {
                "¿cómo estás?": ["Estoy bien, gracias por preguntar.", "¡Estoy aquí para ayudarte!"],
                "¿qué puedes hacer?": ["Puedo responder preguntas y ayudarte con información.", "Soy un asistente virtual que te ayuda con lo que necesites."],
                "¿cuál es tu nombre?": ["Soy un agente virtual sin nombre, pero puedes llamarme Agente.", "No tengo un nombre, pero soy aquí para ayudarte."]
            }
        }
        self.stop_words = set(stopwords.words('spanish'))

    def preprocess(self, message):
        tokens = word_tokenize(message.lower())
        filtered_tokens = [word for word in tokens if word.isalnum() and word not in self.stop_words]
        return filtered_tokens

    def respond(self, message):
        tokens = self.preprocess(message)
        
        if any(token in tokens for token in ["hola", "buenas", "hey"]):
            return random.choice(self.responses["saludos"])
        elif any(token in tokens for token in ["adiós", "hasta", "chau"]):
            return random.choice(self.responses["despedidas"])
        else:
            for question in self.responses["preguntas"]:
                if question in message.lower():
                    return random.choice(self.responses["preguntas"][question])
            return "Lo siento, no entendí tu mensaje. ¿Puedes reformularlo?"

def main():
    agent = ComplexAgent()
    
    print("Agente: ¡Hola! Soy un agente más complejo. Escribe 'adiós' para salir.")
    
    while True:
        user_input = input("Tú: ")
        
        if user_input.lower() in ["adiós", "hasta luego", "chau"]:
            print(agent.respond(user_input))
            break
        
        response = agent.respond(user_input)
        print("Agente:", response)

if __name__ == "__main__":
    main()
