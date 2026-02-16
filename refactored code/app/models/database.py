# database.py

# Simulated in-memory database
quiz_data = [
    {
        "id": 1,
        "question": "Which of the following is an example of AI?",
        "options": ["A calculator performing basic math", "Google Search recommending articles based on your past searches", "A microwave heating food", "A simple alarm clock"],
        "answer": "Google Search recommending articles based on your past searches"
    },
    {
        "id": 2,
        "question": "Which of the following best describes Narrow AI?",
        "options": ["AI that is capable of performing a wide range of tasks like a human", "AI specialized in a specific task, such as voice assistants or recommendation systems", "AI that surpasses human intelligence in all aspects", "AI that does not require training data"],
        "answer": "AI specialized in a specific task, such as voice assistants or recommendation systems"
    },
    {
        "id": 3,
        "question": "What is General AI?",
        "options": ["AI that can perform any intellectual task like a human", "AI that only works for specific tasks", "AI that does not use machine learning.", "AI limited to speech recognition."],
        "answer": "AI that can perform any intellectual task like a human"
    },
    {
        "id": 4,
        "question": "What is Super AI?",
        "options": ["AI that is used in superhero movies", "AI that surpasses human intelligence in all cognitive tasks", "AI that only functions in self-driving cars", "AI with limited problem-solving abilities"],
        "answer": "AI that surpasses human intelligence in all cognitive tasks"
    },
    {
        "id": 5,
        "question": "How is AI different from traditional programming?",
        "options": ["AI follows strict, pre-programmed rules without learning.", "AI does not require data to function", "Traditional programming and AI are the same", "AI can learn from data and improve over time, whereas traditional"],
        "answer": "AI can learn from data and improve over time, whereas traditional"
    },
    {
        "id": 6,
        "question": "What is an example of AI in real-world applications?",
        "options": ["Virtual assistants like Siri and Alexa", "Online recommendation systems", "Self-driving cars", "All of the above"],
        "answer": "All of the above"
    },
    {
        "id": 7,
        "question": "Which of the following is a disadvantage of AI?",
        "options": ["High implementation costs and job displacement", "Increased efficiency and automation", "Faster data analysis", "Improved accuracy in decision-making"],
        "answer": "High implementation costs and job displacement"
    },
    {
        "id": 8,
        "question": "How do AI systems improve their performance over time?",
        "options": ["By rewriting their own source code manually", "By asking humans for corrections every time", "By using feedback and data to adjust their models", "By staying the same after initial training"],
        "answer": "By using feedback and data to adjust their models"
    },
    {
        "id": 9,
        "question": "What role does big data play in AI development?",
        "options": ["It provides a large amount of information that AI models use to learn patterns.", "It slows down AI training due to excessive data.", "AI does not require big data to function.", "Big data is only useful for human analysts, not AI."],
        "answer": "It provides a large amount of information that AI models use to learn patterns."
    },
    {
        "id": 10,
        "question": "How might AI impact the future of work?",
        "options": ["AI will replace all human jobs completely.", "AI will create new job opportunities while automating certain tasks.", "AI will have no impact on jobs or industries.", "AI will only be used in research and not in businesses."],
        "answer": "AI will create new job opportunities while automating certain tasks."
    },
    {
        "id": 11,
        "question": "Which of the following is an application of AI in healthcare?",
        "options": ["Performing manual surgery", "Selling prescription drugs", "Managing hospital staff", "Analyzing medical images for disease detection"],
        "answer": "Analyzing medical images for disease detection"
    },
    {
        "id": 12,
        "question": "How does AI contribute to the finance industry?",
        "options": ["By replacing human bank tellers entirely", "By creating fake credit scores", "By analyzing financial history to predict creditworthiness", "By blocking all online transactions"],
        "answer": "By analyzing financial history to predict creditworthiness"
    },
    {
        "id": 13,
        "question": "Which of the following industries benefits from AI-powered product recommendations?",
        "options": ["Retail", "Agriculture", "Construction", "Aviation"],
        "answer": "Retail"
    },
    {
        "id": 14,
        "question": "What role does AI play in customer service?",
        "options": ["It eliminates the need for human employees", "It powers chatbots that answer customer questions", "It prevents customers from making complaints", "It replaces human supervisors"],
        "answer": "It powers chatbots that answer customer questions"
    },
    {
        "id": 15,
        "question": "Which of the following is a challenge in AI development?",
        "options": ["AI systems are always perfectly fair and unbiased", "AI systems require vast amounts of high-quality data", "AI can work without any computational resources", "AI never faces security threats"],
        "answer": "AI systems require vast amounts of high-quality data"
    },
    {
        "id": 16,
        "question": "Why is interpretability and explainability a challenge in AI?",
        "options": ["AI systems always provide clear explanations for their decisions", "AI never makes mistakes, so explainability is not important", "AI systems sometimes make decisions that are difficult to understand", "AI decisions are always self-explanatory"],
        "answer": "AI systems sometimes make decisions that are difficult to understand"
    },
    {
        "id": 17,
        "question": "How does AI contribute to autonomous vehicles?",
        "options": ["By allowing cars to navigate without human input", "By slowing down traffic deliberately", "By eliminating the need for roads", "By preventing all car accidents"],
        "answer": "By allowing cars to navigate without human input"
    },
    {
        "id": 18,
        "question": "What ethical concern arises from AI’s use in surveillance?",
        "options": ["AI surveillance is always 100% accurate", "AI eliminates the need for human law enforcement", "AI can be misused for mass surveillance and invasion of privacy", "AI removes the need for cybersecurity"],
        "answer": "AI can be misused for mass surveillance and invasion of privacy"
    },
    {
        "id": 19,
        "question": "How does AI contribute to personalized learning?",
        "options": ["By replacing teachers entirely", "By making all students learn at the same pace", "By preventing students from asking questions", "By providing customized educational content based on student needs"],
        "answer": "By providing customized educational content based on student needs"
    },
    {
        "id": 20,
        "question": "What is a potential risk of AI in decision-making?",
        "options": ["AI always makes the best decisions without any issues", "AI decisions may be biased based on the data it was trained on", "AI never requires human oversight", "AI eliminates the need for ethical considerations"],
        "answer": "AI decisions may be biased based on the data it was trained on"
    },

]

# Store user scores (for demo purposes)
user_scores = {}
