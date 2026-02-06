# code-site
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=22140056)

window.open("https://www.example.com", "_blank"); --> sers à ouvrir un page web

mon code à été fait environ à 30% par une intéligence artificielle, voici le prompt que j'ai donné:

could you make it so that every button, only the buttons, change color like the button you just showed me, without changing their position or changing what they do, only make them change color when I click them?
<!-- <!DOCTYPE html>
<html>
<head>
  <style>
    #container {
      display: flex;
      flex-direction: column;
      align-items: center;
      font-family: Arial, sans-serif;
      margin-top: 20px;
    }
    #counter-section, #control-section, #converter-section {
      margin: 10px;
      border: 1px solid #ccc;
      padding: 10px;
      border-radius: 8px;
      width: 350px;
    }
    #counterDisplay {
      font-size: 36px;
      margin: 10px;
    }
    #stateDisplay {
      font-size: 24px;
      margin: 10px;
    }
    button {
      font-size: 20px;
      padding: 8px 12px;
      margin: 5px;
    }
    input[type=number], input[type=text] {
      width: 80px;
      font-size: 24px;
      text-align: center;
      margin-right: 10px;
    }
    select {
      font-size: 16px;
      margin-left: 10px;
    }
  </style>
</head>
<body>
<div id="container">

  <!-- Counter and State Controls -->
  <div id="counter-section">
    <div>Counter: <span id="counterDisplay">0</span></div>
    <div>State (True/False): <span id="stateDisplay">False</span></div>
  </div>

  <!-- Main Controls -->
  <div id="control-section">
    <label for="amountInput">Amount:</label>
    <input id="amountInput" type="number" value="1">
    <div>
      <button id="incrementBtn">Increment (P)</button>
      <button id="decrementBtn">Decrement (M)</button>
    </div>
    <div>
      <button id="toggleBtn">Toggle State</button>
      <button id="resetBtn">Reset</button>
      <button id="enableBtn" disabled>Enable Interaction</button>
    </div>
  </div>

  <!-- Temperature Converter -->
  <div id="converter-section">
    <h3>Temperature Converter</h3>
    <input type="text" id="tempInput" placeholder="Enter temperature">
    <select id="conversionType">
      <option value="f2c">Fahrenheit to Celsius</option>
      <option value="c2f">Celsius to Fahrenheit</option>
    </select>
    <button id="convertBtn">Convert</button>
    <div id="conversionResult" style="margin-top:10px; font-weight:bold;"></div>
  </div>

</div>

<script>
  // Variables
  let counter = 0;
  let state = false; // false = False, true = True

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

  // Function to update displays
  function updateDisplays() {
    counterDisplay.textContent = counter;
    stateDisplay.textContent = state ? 'True' : 'False';
  }

  // All controls for enabling/disabling
  const allControls = [
    incrementBtn, decrementBtn, toggleBtn, resetBtn,
    tempInput, conversionType, convertBtn
  ];

  function disableInteraction() {
    allControls.forEach(el => el.disabled = true);
    enableBtn.disabled = false; // enable button to re-enable
  }

  function enableInteraction() {
    allControls.forEach(el => el.disabled = false);
    enableBtn.disabled = true; // disable enable button
    startInactivityTimer();
  }

  // Event handlers for counter
  document.getElementById('incrementBtn').addEventListener('click', () => {
    const amount = Number(amountInput.value) || 1;
    counter += amount;
    updateDisplays();
  });
  document.getElementById('decrementBtn').addEventListener('click', () => {
    const amount = Number(amountInput.value) || 1;
    counter -= amount;
    updateDisplays();
  });
  document.getElementById('toggleBtn').addEventListener('click', () => {
    state = !state;
    updateDisplays();
  });
  document.getElementById('resetBtn').addEventListener('click', () => {
    counter = 0;
    state = false;
    updateDisplays();
  });
  document.getElementById('enableBtn').addEventListener('click', () => {
    enableInteraction();
  });

  // Temperature conversion
  document.getElementById('convertBtn').addEventListener('click', () => {
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
  });

  // Inactivity timer
  let inactivityTimeout = null;
  const INACTIVITY_TIME = 60000; // 60 seconds

  function startInactivityTimer() {
    clearTimeout(inactivityTimeout);
    inactivityTimeout = setTimeout(() => {
      disableInteraction();
      alert("Inactivity timeout reached. Interaction disabled.");
    }, INACTIVITY_TIME);
  }

  // Add event listeners to all controls to reset timer
  document.querySelectorAll('button, input, select').forEach(el => {
    el.addEventListener('click', () => {
      if (!enableBtn.disabled) {
        startInactivityTimer();
      }
    });
    el.addEventListener('input', () => {
      if (!enableBtn.disabled) {
        startInactivityTimer();
      }
    });
  });

  // Initialize
  updateDisplays();
  enableInteraction(); // start timer at load
</script>
</body>
</html> -->


Le résultat que j'ai obtenu était le suivant: 


(à ajouter dans le code donné:)

(CSS)

/* Add this to your existing CSS */
button {
  transition: background-color 0.2s ease;
}

/* Define original button colors (adjust as needed) */
button {
  background-color: #007bff; /* Blue - adjust to match your design */
  color: white;
}

/* Optional: Different color for disabled state */
button:disabled {
  background-color: #cccccc;
  opacity: 0.6;
  cursor: not-allowed;
}

// Add this code to your existing JavaScript
// Define the highlight color
const highlightColor = '#ff0000'; // Red

// Function to flash button color
function flashButton(button) {
  // Store original color
  const originalColor = button.style.backgroundColor || getComputedStyle(button).backgroundColor;
  
  // Change to highlight color
  button.style.backgroundColor = highlightColor;
  
  // Revert back after 200 milliseconds
  setTimeout(() => {
    button.style.backgroundColor = originalColor;
  }, 200);
}

(JS)

// Add click event listeners to ALL buttons
document.addEventListener('DOMContentLoaded', function() {
  // Get all buttons in the document
  const allButtons = document.querySelectorAll('button');
  
  // Add click event to each button
  allButtons.forEach(button => {
    // Save original click handler
    const originalClick = button.onclick;
    
    // Wrap the click handler to add flash effect
    button.addEventListener('click', function(event) {
      // Flash the button
      flashButton(this);
      
      // Call original click handler if it exists
      if (originalClick) {
        originalClick.call(this, event);
      }
    }, true); // Use capture phase to ensure it runs before other handlers
  });
});