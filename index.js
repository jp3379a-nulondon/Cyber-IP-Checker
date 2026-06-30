// Javascript constants gathered from HTML id's.
const inputForm = document.getElementById("ip-input-form");
const inputBox = document.getElementById("ip-input-field");
const outputBox = document.getElementById("ip-output-field");

// Local Flask server when testing on your machine, Render when live - auto detected.
const api_base =
  location.hostname === "localhost" || location.hostname === "127.0.0.1"
    ? "http://127.0.0.1:5000"
    : "https://cyber-ip-checker.onrender.com";
    
// Removes whitespace from the IP input.
function trimIpAddress(ipAddress) {
  return ipAddress.trim();
}

// Checks whether the API response contains an error.
function getApiErrorMessage(response, data) {
  if (!response.ok || !data.success) {
    return "Error: " + data.error;
  }
  return null;
}

// One labelled bar. Width is the value's share of the total so bars stay meaningful.
// VirusTotal returns vendor counts, not percentages.
function resultBar({ label, color }, value, total) {
  const width = total > 0 ? (value / total) * 100 : 0;
  return `
        <div style="display: flex; align-items: center; gap: 20px; margin: 6px 0;">
            <strong style="width: 90px;">${label}:</strong>
            <span style="width: 32px; text-align: right;">${value}</span>
            <div style="width: 220px; background-color: #ddd; border-radius: 10px;">
                <div style="width: ${width}%; background-color: ${color}; height: 16px; border-radius: 10px;"></div>
            </div>
        </div>`;
}

// Each result category: the field name from the API, its label, and bar colour. 
const categories = [
  { key: "malicious", label: "Malicious", color: "#d90429" },
  { key: "suspicious", label: "Suspicious", color: "#ff9f1c" },
  { key: "undetected", label: "Undetected", color: "#6c757d" },
  { key: "harmless", label: "Harmless", color: "#2e6e37" },
];

// Build the whole results panel from the category list.
function renderResults(results) {
  const total = categories.reduce((sum, c) => sum + results[c.key], 0);
  const bars = categories.map((c) => resultBar(c, results[c.key], total)).join(
    "",
  );
  return `
        <strong>VirusTotal Results for: ${results.ip_address}</strong>
        <div style="display: flex; flex-direction: column; align-items: center;">
            ${bars}
        </div>`;
}

// Fills HTML div element with results in webpage.
function displayOutput(message, isHtml = false) {
  outputBox[isHtml ? "innerHTML" : "textContent"] = message;
}

// Runs when the form is submitted (It reads the IP, calls the API, shows the result)
async function eventHandler(event) {
  event.preventDefault(); // Stop page reload on submit

  const ipAddress = trimIpAddress(inputBox.value); // Removes whitespace on IP input
  displayOutput("Checking IP address..."); // Show a holding message while API is called

  try {
    // Send the IP to server via a POST request
    const response = await fetch(`${api_base}/api/ip-reputation`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ ip_address: ipAddress }),
    });

    const data = await response.json(); // Parse the JSON response

    // Handle errors the server reported
    const errorMessage = getApiErrorMessage(response, data);

    if (errorMessage) {
      displayOutput(errorMessage);
      return;
    }

    displayOutput(renderResults(data.results), true); // Build and show the result bars
  } catch (error) {
    // Live setup message, as render.com server needs to wake up.
    displayOutput(
      "Couldn't reach the server — it may be waking up, try again in a moment.",
    );
  }
}

if (inputForm) {
  inputForm.addEventListener("submit", eventHandler);
}

// For Jest testing - functions exported for testing
if (typeof module !== "undefined") {
  module.exports = {trimIpAddress, getApiErrorMessage}
}