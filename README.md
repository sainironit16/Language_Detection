🌍 Language Detection using Machine Learning

This project is a simple Language Detection System built using Python and Machine Learning. It takes a text input from the user and predicts the language of the given text.

📌 Features
Detects language from user input text
Uses Naive Bayes algorithm for classification
Converts text into numerical features using CountVectorizer
Simple and easy-to-understand implementation
Command-line based interaction
🧠 Technologies Used
Python
Pandas
Scikit-learn
CountVectorizer (for text feature extraction)
Multinomial Naive Bayes (for classification)

⚙️ How It Works
Load the dataset containing text and their respective languages
Convert text data into numerical format using CountVectorizer
Split dataset into training and testing sets
Train the model using Multinomial Naive Bayes
Evaluate model accuracy
Take user input and predict the language

🚀 Installation & Setup
Clone the repository:
git clone https://github.com/your-username/language-detection.git
cd language-detection

Install required libraries:
pip install pandas scikit-learn
Run the program:
python "language detection.py"

📊 Example
Enter the text to predict: Bonjour tout le monde
Output: French

📈 Model Accuracy

The model evaluates accuracy using a test dataset split.
(Your current accuracy will be displayed when you run the script.)
