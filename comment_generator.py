import json
from autogen import ConversableAgent

# Function to load agent data from a JSON file
def load_agent_data(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def create_agent(agent_id, name, agent_instruction):
    return ConversableAgent(
        agent_id,
        system_message=agent_instruction,
        llm_config={"config_list": [{"model": "gpt-4o", "api_key": "sk-XXXXX"}]},
        human_input_mode="NEVER",  # Never ask for human input.
    )

# Function to generate comments from the agent
def generate_comment(agent, prompt):
    reply = agent.generate_reply(messages=[{"content": prompt, "role": "user"}])
    return reply

# Function to get comments from recommended agents
def get_comments_from_agents(recommended_agents, description):
    agent_data = load_agent_data("agent_profiles.json")
    # Create agents for the recommended agent IDs
    agents = []
    for agent_id in recommended_agents:
        print(agent_id)
        agent_info = next((agent for agent in agent_data if agent["id"] == agent_id), None)
        if agent_info:
            agent = create_agent(agent_info["id"], agent_info["name"], agent_info["agent_instruction"])
            agents.append(agent)

    # Generate comments from the agents
    comments = []
    prompt = f"""Sizdən psixoloji portretinizə uyğun olaraq, aşağıda verilən postla bağlı fikirlərinizi 2 sadə və qısa cümlə ilə ifadə etməyinizi xahiş edirik. Bu şərh yazarkən dərin, fəlsəfi və ya mürəkkəb ifadələrdən qaçının. Əsas məqsədiniz sadəcə psixoloji profilinizə uyğun bir reaksiya verməkdir. Təsəvvür edin ki, sosial mediada ya da hər hansı bir platformada qarşınıza bu post çıxıb:
            
            Post Məzmunu: {description}
            
            Şərhinizi yazarkən aşağıdakı məqamları nəzərə alın:

            Sadəlik: Şərhiniz 1-2 cümlədən ibarət olsun və mümkün qədər sadə, emosional və şəxsi olsun.
            Psixoloji Uyğunluq: Şərhiniz psixoloji profilinizə uyğun olsun. Məsələn, əgər optimist bir insansınızsa, şərhiniz daha müsbət ola bilər. Əgər qısqanırsınızsa, bunu birbaşa ifadə etmək əvəzinə, tənqid edərək ört-basdır etməlisiniz. Məsələn, "Bu yaxşıdır, amma bunu paylaşmağın nə mənası var ki" kimi bir ifadə ilə qısqanclığınızı gizlədə bilərsiniz.
            Emosional İfadə: Şərhinizdə öz emosiyalarınızı birbaşa ifadə etməyin. Əvəzində, bu emosiyaları dolayı yolla ifadə edin. Məsələn, kədərli bir vəziyyətdə "Bu çox təsirli deyil" kimi bir şərh yazaraq kədərinizi gizlədə bilərsiniz.
            Tənqidi Yanaşma: Əgər qısqanırsınızsa və ya mənfi bir hiss keçirsinizsə, bunu birbaşa deyil, tənqid edəcək bir şey taparaq ifadə edin. Məsələn, "Bu yaxşıdır, amma daha yaxşı ola bilərdi" kimi bir ifadə ilə qısqanclığınızı gizlədə bilərsiniz. Yəni, şərhdə öz emosiyalarınızı və ya məqsədlərinizi birbaşa ifadə etməyin, əksinə dolayı yolla tənqid edin. 
            Şərhinizi yazıb bitirdikdən sonra, <END> yazın və bu şərhi niyə yazdığınızı bir cümlə ilə səmimi şəkildə izah edin. 
            Nümunə 1:
            Post: Şəkildə çox uğurlu insan öz hekayəsi haqqında danışır.
            OUTPUT: 'Burada nə var ki, bu adamın yüz faiz bəxti gətirib!'
            <END>
            'Mən öz həyatımda uğur qazana bilmədiyim üçün bu insanı qısqandım və bu şərh yazdım.'
            
            Nümunə 3:
            OUTPUT: 'Bu post mənə gülümsətdi. Həyatda belə kiçik şeylərlə də xoşbəxt olmaq olar.'
            <END>
            'Mən optimist bir insanam və kiçik şeylərdən zövq alıram, buna görə bu şərh yazdım.'
            
            Diqqət: Ümumi və ya fəlsəfi şərhlər yazmayın. Əgər sizin system mesajınızda orfoqrafik səhvlər etməyiniz bildirilibsə buna əməl edin, əks halda ignore edin. Əgər bir post görüb mənfi hisslər (məsələn, qısqanclıq, kədər, narazılıq) keçirsənsə, bunu birbaşa yazma. Əvəzində, tənqid edərək və ya dolayı şəkildə öz hisslərini ifadə et. Yalnız psixoloji profilinizə uyğun, emosional və şəxsi bir reaksiya verin (ÜMUMİ VƏ YA FƏLSƏFİ HEÇNƏ YAZMA). Bu tapşırıq sizin daxili dünyanızı və posta olan reaksiyanızı daha yaxşı anlamaq üçün nəzərdə tutulub."""

    for agent in agents:
        comment = generate_comment(agent, prompt)
        comm = comment.split("<END>")[0]
        how_i_felt = comment.split("<END>")[1]
        comments.append({
            "agent_id": agent.name,
            "comment": comm,
            "how_i_felt": how_i_felt
        })

    return comments

