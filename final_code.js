// Variables
let counter = 0;
let state = false;
let inactivityTimeout = null;
const INACTIVITY_TIME = 60000; // 60 seconds

// DOM Elements
const counterDisplay = document.getElementById('counterDisplay');
const stateDisplay = document.getElementById('stateDisplay');
const amountInput = document.getElementById('amountInput');
const incrementBtn = document.getElementById('incrementBtn');
const decrementBtn = document.getElementById('decrementBtn');
const toggleBtn = document.getElementById('toggleBtn');
const resetBtn = document.getElementById('resetBtn');
const enableBtn = document.getElementById('enableBtn');
const tempInput = document.getElementById('tempInput');
const conversionType = document.getElementById('conversionType');
const convertBtn = document.getElementById('convertBtn');
const conversionResult = document.getElementById('conversionResult');

// All controls for enabling/disabling
const allControls = [
    incrementBtn, decrementBtn, toggleBtn, resetBtn,
    tempInput, conversionType, convertBtn
];

// Function to update displays
function updateDisplays() {
    counterDisplay.textContent = counter;
    stateDisplay.textContent = state ? 'True' : 'False';
}

// Inactivity timer functions
function startInactivityTimer() {
    clearTimeout(inactivityTimeout);
    inactivityTimeout = setTimeout(() => {
        disableInteraction();
        alert("Inactivity timeout reached. Interaction disabled.");
    }, INACTIVITY_TIME);
}

function resetInactivityTimer() {
    if (!enableBtn.disabled) { // Only if interactions are enabled
        startInactivityTimer();
    }
}

function disableInteraction() {
    allControls.forEach(el => el.disabled = true);
    enableBtn.disabled = false;
    clearTimeout(inactivityTimeout);
}

function enableInteraction() {
    allControls.forEach(el => el.disabled = false);
    enableBtn.disabled = true;
    startInactivityTimer();
}

// Event handlers for counter
incrementBtn.addEventListener('click', () => {
    const amount = Number(amountInput.value) || 1;
    counter += amount;
    updateDisplays();
    resetInactivityTimer();
});

decrementBtn.addEventListener('click', () => {
    const amount = Number(amountInput.value) || 1;
    counter -= amount;
    updateDisplays();
    resetInactivityTimer();
});

toggleBtn.addEventListener('click', () => {
    state = !state;
    updateDisplays();
    resetInactivityTimer();
});

resetBtn.addEventListener('click', () => {
    counter = 0;
    state = false;
    updateDisplays();
    resetInactivityTimer();
});

enableBtn.addEventListener('click', () => {
    enableInteraction();
});

// Temperature conversion
convertBtn.addEventListener('click', () => {
    const val = parseFloat(tempInput.value);
    if (isNaN(val)) {
        conversionResult.textContent = "Please enter a valid number.";
        return;
    }
    if (conversionType.value === 'f2c') {
        const c = ((val - 32) * 5) / 9;
        conversionResult.textContent = `${val}°F = ${c.toFixed(2)}°C`;
    } else {
        const f = (val * 9) / 5 + 32;
        conversionResult.textContent = `${val}°C = ${f.toFixed(2)}°F`;
    }
    resetInactivityTimer();
});

// Reset timer on any user interaction
document.addEventListener('click', () => {
    // Flash effect for buttons
    if (event.target.tagName === 'BUTTON') {
        const button = event.target;
        const originalColor = button.style.backgroundColor || getComputedStyle(button).backgroundColor;
        const highlightColor = '#ff0000';

        button.style.backgroundColor = highlightColor;
        setTimeout(() => {
            button.style.backgroundColor = originalColor;
        }, 200);
    }
    resetInactivityTimer();
});
document.addEventListener('keydown', resetInactivityTimer);
document.addEventListener('mousemove', resetInactivityTimer);
document.addEventListener('scroll', resetInactivityTimer);

// Initialize
updateDisplays();
enableInteraction(); // start with interactions enabled