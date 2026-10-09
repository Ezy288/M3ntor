import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Special Surprise", 
    layout="centered", 
    initial_sidebar_state="collapsed"
)

# 2. Layout Overrides (Keeps Streamlit components from clipping your site)
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    .block-container {padding: 0px !important; max-width: 100% !important;}
    iframe {border: none; width: 100% !important;}
    </style>
""", unsafe_allow_html=True)

# 3. Complete Mobile Site Source Code
HTML_CONTENT = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Special Surprise for Mentor</title>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            -webkit-tap-highlight-color: transparent;
        }

        body, html {
            width: 100%;
            height: 100%;
            overflow: hidden;
            background-color: #0b132b;
        }

        /* Mobile Simulation Container - Fixed 730px height to stay stable within Streamlit frames */
        .phone-container {
            position: relative;
            width: 100%;
            height: 730px;
            max-width: 430px;
            margin: 0 auto;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            align-items: center;
            padding: 40px 24px;
            background: #0b132b;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            transition: all 0.8s cubic-bezier(0.4, 0, 0.2, 1);
        }

        /* --- SCENE 1 STYLES: ENDLESS HEART TUNNEL --- */
        .tunnel-container {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            overflow: hidden;
            z-index: 1;
            pointer-events: none;
        }

        .tunnel-heart {
            position: absolute;
            top: 50%;
            left: 50%;
            width: 800px;
            height: 800px;
            margin-left: -400px;
            margin-top: -400px;
            opacity: 0;
            animation: tunnelMove 7s linear infinite;
        }

        .tunnel-heart:nth-child(1) { fill: #ffffff; animation-delay: 0s; }
        .tunnel-heart:nth-child(2) { fill: #f0f4f8; animation-delay: 1.4s; }
        .tunnel-heart:nth-child(3) { fill: #d9e2ec; animation-delay: 2.8s; }
        .tunnel-heart:nth-child(4) { fill: #bcccdc; animation-delay: 4.2s; }
        .tunnel-heart:nth-child(5) { fill: #9fb3c8; animation-delay: 5.6s; }

        @keyframes tunnelMove {
            0% { transform: scale(0.01) rotate(0deg); opacity: 0; }
            5% { opacity: 0.8; }
            90% { opacity: 0.8; }
            100% { transform: scale(1.4) rotate(20deg); opacity: 0; }
        }

        /* Floating Welcome Header */
        .welcome-header {
            font-size: 24px;
            font-weight: 800;
            color: #ffffff;
            text-align: center;
            line-height: 1.35;
            z-index: 10;
            margin-top: 10px;
            animation: textFloat 3.5s ease-in-out infinite;
        }

        .welcome-underline {
            width: 70px;
            height: 4px;
            background-color: #829ab1;
            margin: 8px auto 0 auto;
            border-radius: 2px;
        }

        @keyframes textFloat {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
        }

        /* Central Gateway White Heart Structure */
        .heart-wrapper {
            position: relative;
            width: 290px;
            height: 260px;
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 20;
            margin: auto 0;
            transition: transform 0.6s cubic-bezier(0.6, -0.28, 0.735, 0.045), opacity 0.5s;
        }

        .heart-svg {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            fill: #ffffff;
            filter: drop-shadow(0px 10px 20px rgba(0, 0, 0, 0.2));
        }

        .heart-content {
            position: relative;
            z-index: 35;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            width: 100%;
            height: 100%;
            padding-top: 5px; 
            padding-bottom: 25px; 
        }

        .answer-input {
            width: 160px;
            padding: 10px 14px;
            border: 2px solid #bcccdc;
            border-radius: 20px;
            text-align: center;
            font-size: 15px;
            color: #334e68;
            outline: none;
            background-color: #f0f4f8;
            margin-bottom: 10px;
            box-shadow: inset 0 2px 4px rgba(0,0,0,0.05);
        }

        .enter-btn {
            background: linear-gradient(135deg, #627d98, #486581);
            color: white;
            border: none;
            padding: 9px 26px;
            font-size: 14px;
            font-weight: bold;
            border-radius: 18px;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(72, 101, 129, 0.4);
        }

        /* Light Blue Styled Clue Container */
        .instructions-text {
            font-size: 14px;
            color: #102a43;
            font-weight: 600;
            text-align: center;
            line-height: 1.45;
            background: rgba(217, 226, 236, 0.95);
            border-left: 5px solid #627d98;
            padding: 14px 18px;
            border-radius: 12px;
            z-index: 10;
            max-width: 95%;
            box-shadow: 0 8px 16px rgba(0,0,0,0.15);
        }

        .blackout-mask {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: #000000;
            opacity: 0;
            z-index: 90;
            pointer-events: none;
            transition: opacity 0.4s ease;
        }

        /* --- SCENE 2 STYLES: DARK MODE TYPING LETTER --- */
        .scene-stage {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 30px 20px;
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.6s ease, transform 0.4s ease;
            z-index: 40;
        }

        .active-stage {
            opacity: 1;
            pointer-events: auto;
        }

        .dark-letter-card {
            width: 100%;
            max-height: 70vh;
            background: #1f2937;
            border: 1px solid #374151;
            border-radius: 20px;
            padding: 24px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.4);
            display: flex;
            flex-direction: column;
            color: #f3f4f6;
            overflow-y: auto;
        }

        .letter-title {
            font-size: 22px;
            color: #60a5fa;
            margin-bottom: 16px;
            font-weight: bold;
            border-bottom: 1px dashed #4b5563;
            padding-bottom: 8px;
        }

        .typing-content {
            font-size: 15px;
            line-height: 1.6;
            color: #e5e7eb;
            white-space: pre-wrap;
        }

        .slide-next-btn {
            margin-top: 20px;
            background: #374151;
            color: #9ca3af;
            font-size: 20px;
            padding: 10px 40px;
            border-radius: 30px;
            border: 2px solid #4b5563;
            cursor: pointer;
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
        }

        /* --- SCENE 3 STYLES: THE JUMPING PROPOSAL SCREEN --- */
        .proposal-card {
            text-align: center;
            z-index: 50;
            width: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .jumping-heart-box {
            animation: heartJump 1.8s cubic-bezier(0.25, 1, 0.5, 1) infinite;
            margin-bottom: 20px;
        }

        @keyframes heartJump {
            0%, 100% { transform: translateY(0) scale(1); }
            40% { transform: translateY(-30px) scale(1.05); }
            70% { transform: translateY(0) scale(0.95); }
        }

        .proposal-question {
            font-size: 22px;
            font-weight: bold;
            color: #ffffff;
            margin-bottom: 30px;
        }

        .choice-btn-stack {
            display: flex;
            flex-direction: column;
            gap: 14px;
            width: 80%;
        }

        .choice-btn {
            padding: 14px;
            font-size: 16px;
            font-weight: bold;
            border-radius: 25px;
            border: none;
            cursor: pointer;
        }

        .btn-promise {
            background: linear-gradient(135deg, #3b82f6, #1d4ed8);
            color: white;
        }

        .btn-cant {
            background: #374151;
            color: #9ca3af;
            border: 1px solid #4b5563;
            position: relative;
        }

        .btn-cant.crossed-out {
            text-decoration: line-through;
            color: #ef4444 !important;
            border-color: #ef4444 !important;
            opacity: 0.6;
        }

        .btn-cant.crossed-out::after {
            content: '❌';
            position: absolute;
            right: 15px;
            top: 50%;
            transform: translateY(-50%);
        }

        .final-success-box {
            background: #1f2937;
            border: 2px solid #10b981;
            border-radius: 20px;
            padding: 20px;
            color: #10b981;
            font-size: 18px;
            font-weight: bold;
            text-align: center;
            margin-top: 25px;
            display: none;
        }

        .final-success-box.show {
            display: block;
        }

        .feedback-toast {
            position: absolute;
            top: 30px;
            background-color: #ef4444;
            color: white;
            padding: 12px 24px;
            border-radius: 25px;
            font-weight: bold;
            font-size: 14px;
            opacity: 0;
            transform: translateY(-30px);
            transition: all 0.3s ease;
            z-index: 100;
            pointer-events: none;
        }

        .feedback-toast.show {
            opacity: 1;
            transform: translateY(0);
        }

        #confettiCanvas {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 80;
        }
    </style>
</head>
<body>
    <div class="phone-container" id="appFrame">
        <div class="feedback-toast" id="toastMessage">Incorrect and access denied</div>
        <canvas id="confettiCanvas"></canvas>
        <div class="blackout-mask" id="blackout"></div>
        
        <div class="tunnel-container" id="tunnelBackground">
            <svg class="tunnel-heart" viewBox="0 0 32 29.6"><path d="M23.6,0c-3.4,0-6.3,2.7-7.6,5.6C14.7,2.7,11.8,0,8.4,0C3.8,0,0,3.8,0,8.4c0,9.4,9.5,11.9,16,21.2c6.1-9.3,16-12.1,16-21.2C32,3.8,28.2,0,23.6,0z"/></svg>
            <svg class="tunnel-heart" viewBox="0 0 32 29.6"><path d="M23.6,0c-3.4,0-6.3,2.7-7.6,5.6C14.7,2.7,11.8,0,8.4,0C3.8,0,0,3.8,0,8.4c0,9.4,9.5,11.9,16,21.2c6.1-9.3,16-12.1,16-21.2C32,3.8,28.2,0,23.6,0z"/></svg>
            <svg class="tunnel-heart" viewBox="0 0 32 29.6"><path d="M23.6,0c-3.4,0-6.3,2.7-7.6,5.6C14.7,2.7,11.8,0,8.4,0C3.8,0,0,3.8,0,8.4c0,9.4,9.5,11.9,16,21.2c6.1-9.3,16-12.1,16-21.2C32,3.8,28.2,0,23.6,0z"/></svg>
            <svg class="tunnel-heart" viewBox="0 0 32 29.6"><path d="M23.6,0c-3.4,0-6.3,2.7-7.6,5.6C14.7,2.7,11.8,0,8.4,0C3.8,0,0,3.8,0,8.4c0,9.4,9.5,11.9,16,21.2c6.1-9.3,16-12.1,16-21.2C32,3.8,28.2,0,23.6,0z"/></svg>
            <svg class="tunnel-heart" viewBox="0 0 32 29.6"><path d="M23.6,0c-3.4,0-6.3,2.7-7.6,5.6C14.7,2.7,11.8,0,8.4,0C3.8,0,0,3.8,0,8.4c0,9.4,9.5,11.9,16,21.2c6.1-9.3,16-12.1,16-21.2C32,3.8,28.2,0,23.6,0z"/></svg>
        </div>

        <div class="welcome-header" id="welcBlock">
            Welcome again mentor!<br>I have made another surprise for you~
            <div class="welcome-underline"></div>
        </div>

        <div class="heart-wrapper" id="gatewayHeart">
            <svg class="heart-svg" viewBox="0 0 32 29.6"><path d="M23.6,0c-3.4,0-6.3,2.7-7.6,5.6C14.7,2.7,11.8,0,8.4,0C3.8,0,0,3.8,0,8.4c0,9.4,9.5,11.9,16,21.2c6.1-9.3,16-12.1,16-21.2C32,3.8,28.2,0,23.6,0z"/></svg>
            <div class="heart-content">
                <input type="text" class="answer-input" id="pwdField" placeholder="Enter answer" autocomplete="off">
                <button class="enter-btn" id="submitBtn">Enter</button>
            </div>
        </div>

        <div class="instructions-text" id="instructBlock">
            To continue, you must figure out what our fav colors will equal to if combined then input ur answer in the heart!~ (˶ᴖ ᴗ ᴖ˶)
        </div>

        <div class="scene-stage" id="stageScene2">
            <div class="dark-letter-card">
                <div class="letter-title">For you &lt;3</div>
                <div class="typing-content" id="letterBody"></div>
            </div>
            <button class="slide-next-btn" id="slideBtn">⮞⮞⮞</button>
        </div>

        <div class="scene-stage" id="stageScene3">
            <div class="proposal-card">
                <div class="jumping-heart-box">
                    <svg width="70" height="65" viewBox="0 0 32 29.6" style="fill: #60a5fa; filter: drop-shadow(0 4px 10px rgba(96,165,250,0.5));"><path d="M23.6,0c-3.4,0-6.3,2.7-7.6,5.6C14.7,2.7,11.8,0,8.4,0C3.8,0,0,3.8,0,8.4c0,9.4,9.5,11.9,16,21.2c6.1-9.3,16-12.1,16-21.2C32,3.8,28.2,0,23.6,0z"/></svg>
                </div>
                <div class="proposal-question">Promise to be my life-time partner?</div>
                <div class="choice-btn-stack">
                    <button class="choice-btn btn-promise" id="promiseBtn">Promise</button>
                    <button class="choice-btn btn-cant" id="cantBtn">I can't..</button>
                </div>
            </div>
            <div class="final-success-box" id="victoryBox">Hehe! I knew you wouldn't let me down</div>
        </div>
    </div>

    <script>
        const submitBtn = document.getElementById('submitBtn');
        const pwdField = document.getElementById('pwdField');
        const toast = document.getElementById('toastMessage');
        const appFrame = document.getElementById('appFrame');
        const blackout = document.getElementById('blackout');
        const welcBlock = document.getElementById('welcBlock');
        const gatewayHeart = document.getElementById('gatewayHeart');
        const instructBlock = document.getElementById('instructBlock');
        const tunnelBackground = document.getElementById('tunnelBackground');
        const stageScene2 = document.getElementById('stageScene2');
        const letterBody = document.getElementById('letterBody');
        const slideBtn = document.getElementById('slideBtn');
        const stageScene3 = document.getElementById('stageScene3');
        const promiseBtn = document.getElementById('promiseBtn');
        const cantBtn = document.getElementById('cantBtn');
        const victoryBox = document.getElementById('victoryBox');

        const secretKeys = ["light blue", "Light Blue", "Light blue"];
        const letterText = "My favorite place is always by your side. You're the coolest mentor! I always notice that you say sorry alot which is a really bad habit! You don’t have to apologize for existing, or for making simple mistakes. That's what makes you human! You always manage to deliver me the reassurance that i need everytime successfully, even when i dont ask for it :0 Haha, so what i'm trying to say is i love you from the deepest part of my heart but.. its not like I mean it or anything!! (˶˃⤙˂˶) Well.. I'll always love you Arif, even if you were to get reinc4rnated as some weird lookin creature.";
        let rejectClickCount = 0;

        function verifyGatewayPassword() {
            const entry = pwdField.value.trim();
            if (secretKeys.includes(entry)) { executeCinematicTransition(); } 
            else { displayToast("Incorrect and access denied"); }
        }
        function displayToast(msg) {
            toast.textContent = msg; toast.classList.add('show');
            setTimeout(() => toast.classList.remove('show'), 2000);
        }
        function executeCinematicTransition() {
            gatewayHeart.style.transform = "scale(8)"; gatewayHeart.style.opacity = "0";
            welcBlock.style.opacity = "0"; instructBlock.style.opacity = "0"; tunnelBackground.style.opacity = "0";
            setTimeout(() => { blackout.style.opacity = "1"; }, 250);
            setTimeout(() => {
                welcBlock.style.display = "none"; gatewayHeart.style.display = "none"; instructBlock.style.display = "none"; tunnelBackground.style.display = "none";
                appFrame.style.background = "linear-gradient(to bottom, #ffb6c1 0%, #ffffff 50%, #8e8e93 100%)";
                blackout.style.opacity = "0";
                stageScene2.classList.add('active-stage');
                startSlowerTyping();
            }, 800);
        }
        function startSlowerTyping() {
            let index = 0; const writingSpeed = 45; 
            function typeChar() {
                if (index < letterText.length) {
                    letterBody.textContent += letterText.charAt(index);
                    index++; setTimeout(typeChar, writingSpeed);
                }
            }
            setTimeout(typeChar, 400);
        }
        slideBtn.addEventListener('click', () => {
            stageScene2.style.transform = "translateX(100%)"; stageScene2.style.opacity = "0";
            setTimeout(() => { stageScene2.classList.remove('active-stage'); stageScene3.classList.add('active-stage'); }, 400);
        });
        cantBtn.addEventListener('click', () => {
            if (rejectClickCount === 0) { displayToast("Why not? :‹"); rejectClickCount++; } 
            else if (rejectClickCount === 1) { cantBtn.classList.add('crossed-out'); cantBtn.disabled = true; }
        });
        promiseBtn.addEventListener('click', () => {
            victoryBox.classList.add('show'); cantBtn.style.display = "none"; promiseBtn.style.display = "none";
            initiateHighDensityConfetti();
        });
        
        submitBtn.addEventListener('click', (e) => { e.preventDefault(); verifyGatewayPassword(); });
        pwdField.addEventListener('keypress', (e) => { if (e.key === 'Enter') verifyGatewayPassword(); });

        const canvas = document.getElementById("confettiCanvas"); const ctx = canvas.getContext("2d");
        let confettiArray = [];
        function resizeCanvas() { canvas.width = appFrame.clientWidth; canvas.height = appFrame.clientHeight; }
        window.addEventListener('resize', resizeCanvas); resizeCanvas();

        class ConfettiParticle {
            constructor() {
                this.x = Math.random() * canvas.width; this.y = canvas.height + Math.random() * 50;
                this.size = Math.random() * 7 + 4; this.speedY = -Math.random() * 6 - 4; this.speedX = Math.random() * 4 - 2;
                this.rotation = Math.random() * 360; this.rotationSpeed = Math.random() * 4 - 2;
                const colors = ['#60a5fa', '#3b82f6', '#eff6ff', '#9ca3af', '#f3f4f6', '#ef4444'];
                this.color = colors[Math.floor(Math.random() * colors.length)];
            }
            update() { this.y += this.speedY; this.x += this.speedX; this.rotation += this.rotationSpeed; this.speedY += 0.08; }
            draw() {
                ctx.save(); ctx.translate(this.x, this.y); ctx.rotate((this.rotation * Math.PI) / 180);
                ctx.fillStyle = this.color; ctx.fillRect(-this.size / 2, -this.size / 2, this.size, this.size); ctx.restore();
            }
        }
        function initiateHighDensityConfetti() {
            for (let i = 0; i < 180; i++) { confettiArray.push(new ConfettiParticle()); }
            animateConfettiLoop();
            const generatorInterval = setInterval(() => {
                if(confettiArray.length < 300) { for(let i=0; i<15; i++) confettiArray.push(new ConfettiParticle()); }
            }, 100);
            setTimeout(() => { clearInterval(generatorInterval); }, 6000);
        }
        function animateConfettiLoop() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            for (let i = 0; i < confettiArray.length; i++) {
                confettiArray[i].update(); confettiArray[i].draw();
                if (confettiArray[i].y > canvas.height + 20) { confettiArray.splice(i, 1); i--; }
            }
            requestAnimationFrame(animateConfettiLoop);
        }
    </script>
</body>
</html>
"""

st.components.v1.html(HTML_CONTENT, height=740, scrolling=False)
