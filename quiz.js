let score = 0;
let currentQuestion = 1;

function startQuiz() {
    document.getElementById('quiz-container').classList.remove('hidden');
    document.getElementById('result-container').classList.add('hidden');
    showQuestion();
}

function showQuestion() {
    document.getElementById('question').innerText = getQuestionText(currentQuestion);
    document.getElementById('answer').value = '';
}

function checkAnswer() {
    const userAnswer = document.getElementById('answer').value.toLowerCase();

    if (userAnswer === getCorrectAnswer(currentQuestion).toLowerCase()) {
        score++;
    }

    currentQuestion++;

    if (currentQuestion <= totalQuestions) {
        showQuestion();
    } else {
        showResult();
    }
}

function showResult() {
    document.getElementById('quiz-container').classList.add('hidden');
    document.getElementById('result-container').classList.remove('hidden');

    document.getElementById('result').innerText = `You got ${score} questions correct!`;
    document.getElementById('score').innerText = `You got ${(score / totalQuestions) * 100}%.`;
}

// Helper functions (replace these with your actual quiz data)
function getQuestionText(questionNumber) {
    const questions = [
        "What does CPU stand for?",
        "What does AWS stand for?",
        "What is the opposite of North?"
    ];

    return questions[questionNumber - 1];
}

function getCorrectAnswer(questionNumber) {
    const answers = [
        "Central Processing Unit",
        "Amazon Web Services",
        "South"
    ];

    return answers[questionNumber - 1];
}

const totalQuestions = 3;
