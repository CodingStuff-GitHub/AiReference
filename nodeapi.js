import dotenv from "dotenv";
import { GoogleGenerativeAI } from "@google/generative-ai";

dotenv.config({ path: "config.env" });

const genAI = new GoogleGenerativeAI(process.env.GEMINI_KEY);
const model = genAI.getGenerativeModel({ model: "gemini-pro" });

async function run() {
    const prompt = "Write a story about a magic backpack."
    const result = await model.generateContent(prompt);
    const response = result.response;
    const text = response.text();
    console.log(text);
}

run();
