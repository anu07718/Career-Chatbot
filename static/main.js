function getCareer() {
  const interest = document.getElementById("interestInput").value;

  fetch("/get-career", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ interest })
  })
    .then(res => res.json())
    .then(data => {
      const output = document.getElementById("output");
      if (data.error) {
        output.innerHTML = `<p>${data.error}</p>`;
        return;
      }

      output.innerHTML = `
        <h3>🧑‍💼 Suggested Careers:</h3>
        <ul>${data.careers.map(c => `<li>${c}</li>`).join("")}</ul>
        <p><strong>✨ Key Features:</strong> ${data.features}</p>
        <h4>📌 Career Roadmap</h4>
        <img src="${data.image}" alt="Career Roadmap"/>
      `;
    });
}
