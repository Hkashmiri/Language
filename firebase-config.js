// firebase-config.js
import { initializeApp } from "https://www.gstatic.com/firebasejs/11.4.0/firebase-app.js";
import { getAuth } from "https://www.gstatic.com/firebasejs/11.4.0/firebase-auth.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/11.4.0/firebase-analytics.js";

// Firebase configuration


const firebaseConfig = {
    apiKey: "AIzaSyDdv1-vbGrQoSbK5f0ATIhrjGUggfrUwN8",
    authDomain: "language-labyrinth.firebaseapp.com",
    projectId: "language-labyrinth",
    storageBucket: "language-labyrinth.appspot.com",  // Fixed typo here
    messagingSenderId: "309364119548",
    appId: "1:309364119548:web:e6b3ad6f18001e91228479",
    measurementId: "G-CNF2B4YPQX"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
const auth = getAuth(app); // Authentication instance

export { auth };
