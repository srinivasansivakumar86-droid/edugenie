async function sendRequest(url, data, resultId) {

    const resultBox = document.getElementById(resultId);

    resultBox.innerText = "⏳ Generating response...";

    try {

        const response = await fetch(url, {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (!response.ok) {
            throw new Error(result.detail || "Something went wrong");
        }

        resultBox.innerText = result.result;

    } catch (error) {

        resultBox.innerText =
            "❌ Error: " + error.message;
    }
}


/* Ask EduGenie */

function askQuestion() {

    const question =
        document.getElementById("question").value.trim();

    if (!question) {
        alert("Please enter your question.");
        return;
    }

    sendRequest(
        "/qa",
        {
            prompt: question
        },
        "qaResult"
    );
}


/* Explain Topic */

function explainTopic() {

    const topic =
        document.getElementById("explainTopic").value.trim();

    const level =
        document.getElementById("explainLevel").value;

    if (!topic) {
        alert("Please enter a topic.");
        return;
    }

    sendRequest(
        "/explain",
        {
            topic: topic,
            level: level
        },
        "explainResult"
    );
}


/* Generate Quiz */

function generateQuiz() {

    const topic =
        document.getElementById("quizTopic").value.trim();

    const numberOfQuestions =
        Number(document.getElementById("quizNumber").value);

    const difficulty =
        document.getElementById("quizDifficulty").value;

    if (!topic) {
        alert("Please enter a quiz topic.");
        return;
    }

    sendRequest(
        "/quiz",
        {
            topic: topic,
            number_of_questions: numberOfQuestions,
            difficulty: difficulty
        },
        "quizResult"
    );
}


/* Summarize */

function summarizeText() {

    const text =
        document.getElementById("summaryText").value.trim();

    if (!text) {
        alert("Please paste your study material.");
        return;
    }

    sendRequest(
        "/summarize",
        {
            text: text
        },
        "summaryResult"
    );
}


/* Learning Path */

function createLearningPath() {

    const topic =
        document.getElementById("learningTopic").value.trim();

    const level =
        document.getElementById("learningLevel").value;

    const duration =
        document.getElementById("learningDuration").value;

    if (!topic) {
        alert("Please enter a learning topic.");
        return;
    }

    sendRequest(
        "/learn/recommendations",
        {
            topic: topic,
            level: level,
            duration: duration
        },
        "learningResult"
    );
}