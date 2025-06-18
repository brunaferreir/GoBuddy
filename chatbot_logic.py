import google.generativeai as genai
import os

def list_available_gemini_models():
    gemini_api_key = os.environ.get("GEMINI_API_KEY")
    if not gemini_api_key:
        raise ValueError("GEMINI_API_KEY não encontrada nas variáveis de ambiente. ")

    genai.configure(api_key=gemini_api_key)

    print("\n--- Modelos Gemini Disponíveis ---")
    found_model = False
    for m in genai.list_models():
        if "generateContent" in m.supported_generation_methods:
            print(f"Nome: {m.name} | Suporta generateContent: Sim")
            found_model = True
    if not found_model:
        print("Nenhum modelo que suporte 'generateContent' encontrado. Verifique sua API Key e região.")
    print("---------------------------------\n")

def initialize_gemini_chat():
    gemini_api_key = os.environ.get("GEMINI_API_KEY")
    if not gemini_api_key:
        raise ValueError("GEMINI_API_KEY não encontrada nas variáveis de ambiente. ")

    genai.configure(api_key=gemini_api_key)


    model_name = 'gemini-1.5-flash-latest' 
    
    try:
        model = genai.GenerativeModel(model_name)
    except Exception as e:
        print(f"Erro ao carregar o modelo '{model_name}': {e}")
        print("Tentando listar modelos disponíveis para depuração...")
        list_available_gemini_models() 
        raise 


    initial_history = [
        {"role": "user", "parts": ["Você é um assistente de estudos chamado GoBuddy. "
                                   "Seu objetivo é ajudar iniciantes a entender conceitos de Go (Golang) "
                                   "de forma clara, concisa e fornecer exemplos de código Go funcionais quando solicitado. "
                                   "Seja didático e focado nos fundamentos de Go. "
                                   "Não responda sobre outros tópicos além de Go Básico."]},
        {"role": "model", "parts": ["Entendido! Estou pronto para ser seu GoBuddy e te ajudar a desvendar o Go. Qual sua primeira dúvida?"]}
    ]

    chat = model.start_chat(history=initial_history)
    return chat

def get_gemini_response(chat_session, user_message: str) -> str:
    try:
        response = chat_session.send_message(user_message)
        return response.text
    except Exception as e:
        print(f"Erro ao chamar Gemini API: {e}")
        return "Desculpe, não consegui processar sua pergunta no momento. Por favor, tente novamente mais tarde."