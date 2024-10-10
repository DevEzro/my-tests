class SimpleAgent:
    def __init__(self):
        self.greetings = ["hola", "buenas", "hey"]
        self.farewells = ["adiós", "hasta luego", "chau"]
        
    def respond(self, message):
        message = message.lower()
        
        if any(greet in message for greet in self.greetings):
            return "¡Hola! ¿Cómo puedo ayudarte hoy?"
        elif any(farewell in message for farewell in self.farewells):
            return "¡Hasta luego! Que tengas un buen día."
        else:
            return "Lo siento, no entendí tu mensaje."

def main():
    agent = SimpleAgent()
    
    print("Agente: ¡Hola! Soy un agente simple. Escribe 'adiós' para salir.")
    
    while True:
        user_input = input("Tú: ")
        
        if user_input.lower() in ["adiós", "hasta luego", "chau"]:
            print(agent.respond(user_input))
            break
        
        response = agent.respond(user_input)
        print("Agente:", response)

if __name__ == "__main__":
    main()