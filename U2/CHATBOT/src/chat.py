class Chatbot:
    def __init__(self):
        self.questions = [
            "¿El motor hace ruidos extraños? (No/Poco/Si)",
            "¿Hay alguna luz de advertencia encendida en el tablero? (No/Si)",
            "¿El auto tiene problemas para arrancar? (No/Poco/Si)",
            "¿El auto se sacude o vibra al conducir? (No/Poco/Si)",
            "¿Hay fugas de líquidos bajo el auto? (No/Poco/Si)",
            "¿La dirección se siente más dura o más suelta de lo normal? (No/Poco/Si)",
            "¿La transmisión hace ruidos o cambios bruscos? (No/Poco/Si)",
            "¿Notas algún olor inusual dentro del auto? (No/Poco/Si)",
            "¿Los frenos chirrían o hacen ruidos al frenar? (No/Poco/Si)",
            "¿Has notado alguna pérdida de potencia en el motor? (No/Poco/Si)",
            "¿El consumo de combustible ha aumentado recientemente? (No/Poco/Si)",
            "¿El volante está desalineado o vibrando? (No/Poco/Si)",
            "¿Has sentido alguna vibración inusual en el pedal del freno? (No/Poco/Si)",
            "¿El vehículo se inclina hacia un lado al frenar? (No/Si)",
            "¿Ha habido cambios en el comportamiento de la suspensión? (No/Si)",
            "¿Has tenido algún problema con el sistema eléctrico? (No/Si)",
            "¿El nivel de aceite del motor es adecuado? (No/Si)",
            "¿Has notado alguna anomalía en el funcionamiento de las luces? (No/Si)",
            "¿La batería del auto se ha descargado recientemente? (No/Si)",
        ]

    def ask_questions(self):
        answers = []
        for question in self.questions:
            answer = input(question + ": ").capitalize()
            if question.startswith("¿El vehículo se inclina hacia un lado al frenar?") or question.startswith("¿Ha habido cambios en el comportamiento de la suspensión?") or question.startswith("¿Has tenido algún problema con el sistema eléctrico?") or question.startswith("¿El nivel de aceite del motor es adecuado?") or question.startswith("¿Has notado alguna anomalía en el funcionamiento de las luces?") or question.startswith("¿La batería del auto se ha descargado recientemente?"):
                while answer not in ["No", "Si"]:
                    print("Por favor, responde 'No' o 'Si'.")
                    answer = input(question + ": ").capitalize()
            else:
                while answer not in ["No", "Poco", "Si"]:
                    print("Por favor, responde 'No', 'Poco' o 'Si'.")
                    answer = input(question + ": ").capitalize()
            answers.append(answer)
        return answers

    def recommend_mechanic(self, answers):
        # Crear un contador para evaluar la gravedad de las respuestas
        severity_count = {"No": 0, "Poco": 0, "Si": 0}

        for answer in answers:
            severity_count[answer] += 1

        # Evaluar la gravedad general del problema
        if severity_count["Si"] >= 3:
            print("Es muy recomendable llevar el auto al mecánico de inmediato para una revisión exhaustiva.")
        elif severity_count["Si"] >= 1 or severity_count["Poco"] >= 3:
            print("Sería prudente hacer una revisión en el taller para asegurarte de que todo esté en orden.")
        else:
            print("Tu auto parece estar en buenas condiciones, pero asegúrate de realizar un mantenimiento regular.")

if __name__ == "__main__":
    chatbot = Chatbot()
    print("¡Hola! Responde algunas preguntas sobre el funcionamiento de tu auto.")
    answers = chatbot.ask_questions()
    chatbot.recommend_mechanic(answers)