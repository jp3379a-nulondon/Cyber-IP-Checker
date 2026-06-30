/**
 * @jest-environment jsdom
 */

const { trimIpAddress, getApiErrorMessage } = require("./index.js");

describe("Tests in Jest", () => {
  test("Smoke Test - make sure jest is working", () => {
    expect(2 + 2).toBe(4);
  });

  test("Test function to check whitespace is trimmed from inputted IP address", () => {
    expect(trimIpAddress("   8.8.8.8   ")).toBe("8.8.8.8");
  });

  test("Test function on error error message when the API response is unsuccessful", () => {
    const response = {
      ok: false, // Create fake API result which failed
    };

    const data = {
      success: false,
      error: "Invalid IP address", // Creates a fake API response
    };

    // The expected result
    expect(getApiErrorMessage(response, data)).toBe(
      "Error: Invalid IP address"
    );
  });
});