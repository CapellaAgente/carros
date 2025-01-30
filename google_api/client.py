import google.generativeai as genai

key = 'insert your API'

def car_bio_ai(model, brand, year):
    genai.configure(api_key = key)
    model_ai = genai.GenerativeModel('gemini-1.5-flash')

    message = 'Crie uma descrição de venda sobre o carro {} {} {}, em até 200 caracteres. Diga coisas específicas do carro e coisas interessantes que ele tem, evite repetir palavras.'
    message = message.format(brand, model, year)
    response = model_ai.generate_content(message)   
    return response.text