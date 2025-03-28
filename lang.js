import OpenAI from 'openai';
import fs from 'fs';
import difflib from 'difflib';

// Set your OpenAI API key
const openai = new OpenAI({ apiKey: 'your-api-key-here' });

async function transcribeAudio(audioFilePath) {
    const audioFile = fs.createReadStream(audioFilePath);
    const response = await openai.audio.transcriptions.create({
        model: "whisper-1",
        file: audioFile
    });
    return response.text;
}

function checkPronunciation(transcribedText, expectedText) {
    const expectedWords = expectedText.toLowerCase().split(" ");
    const spokenWords = transcribedText.toLowerCase().split(" ");

    let incorrectWords = [];
    spokenWords.forEach(spokenWord => {
        if (!expectedWords.includes(spokenWord)) {
            const closestMatch = difflib.getCloseMatches(spokenWord, expectedWords, 1);
            incorrectWords.push({ incorrect: spokenWord, suggested: closestMatch[0] || "(No close match)" });
        }
    });

    return incorrectWords;
}

async function main(audioFilePath, expectedText) {
    console.log("Transcribing audio...");
    const transcribedText = await transcribeAudio(audioFilePath);
    console.log("Transcribed Text:", transcribedText);

    const incorrectWords = checkPronunciation(transcribedText, expectedText);

    if (incorrectWords.length > 0) {
        console.log("\nPronunciation Feedback:");
        incorrectWords.forEach(({ incorrect, suggested }) => {
            console.log(`Incorrect: '${incorrect}' | Suggested: '${suggested}'`);
        });
    } else {
        console.log("Great pronunciation! No mistakes found.");
    }
}

const audioPath = process.argv[2];
const expectedSentence = process.argv[3];
if (audioPath && expectedSentence) {
    main(audioPath, expectedSentence);
} else {
    console.log("Usage: node script.js <audioFilePath> <expectedText>");
}
