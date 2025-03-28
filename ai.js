import fs from "fs";
import OpenAI from "openai";
import dotenv from "dotenv";
dotenv.config(); 


const openai = new OpenAI({
    apiKey: process.env.OPENAI_API_KEY, // Use environment variable
});

async function main() {
    const translation = await openai.audio.translations.create({
        file: fs.createReadStream("audio/lessonfive/01 Lesson 01.mp3"),
        model: "whisper-1",
    });

    console.log(translation.text);
}
main();