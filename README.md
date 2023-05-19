Certainly! I can provide you with a basic example of two websites—one acting as the data input site and the other as the data receiving site.

Website 1 (Data Input Site):
Create a new HTML file called index.html and add the following code:

html
Copy code
<!DOCTYPE html>
<html>
<head>
  <title>Data Input Site</title>
</head>
<body>
  <h1>Data Input Site</h1>
  <form action="http://localhost:3000/forward-data" method="POST">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required><br>
    <label for="family-name">Family Name:</label>
    <input type="text" id="family-name" name="familyName" required><br>
    <label for="registration-plate">Registration Plate:</label>
    <input type="text" id="registration-plate" name="registrationPlate" required><br>
    <label for="card-number">Credit Card Number:</label>
    <input type="text" id="card-number" name="cardNumber" required><br>
    <button type="submit">Submit</button>
  </form>
</body>
</html>
This code represents the data input site where users can fill in their information, including name, family name, registration plate, and credit card number. The form action is set to http://localhost:3000/forward-data, which is the endpoint of the data receiving site.

Website 2 (Data Receiving Site):
Create a new HTML file called index.html and add the following code:

html
Copy code
<!DOCTYPE html>
<html>
<head>
  <title>Data Receiving Site</title>
</head>
<body>
  <h1>Data Receiving Site</h1>
  <div id="data-container">
    <p>Data will be displayed here after submission.</p>
  </div>

  <script>
    fetch('http://localhost:3000/forward-data')
      .then(response => response.json())
      .then(data => {
        const dataContainer = document.getElementById('data-container');
        dataContainer.innerHTML = `
          <p>Name: ${data.name}</p>
          <p>Family Name: ${data.familyName}</p>
          <p>Registration Plate: ${data.registrationPlate}</p>
          <p>Credit Card Number: ${data.cardNumber}</p>
        `;
      })
      .catch(error => {
        console.error('Error:', error);
      });
  </script>
</body>
</html>
This code represents the data receiving site. It fetches the data from http://localhost:3000/forward-data, assuming the data forwarding server is running locally. The received data is then displayed on the page.

To test the setup:

Follow the steps mentioned earlier to set up the data forwarding server by creating an index.js file with the provided code and running node index.js in the terminal.

Open the first website (index.html) in your browser. Fill in the form fields and submit the form.

Open the second website (index.html) in another browser tab or window. The submitted data should be displayed on the page.

Remember to replace the URL (http://localhost:3000/forward-data) with the appropriate URL if you're hosting the data forwarding server elsewhere.

Please note that this is a basic demonstration to showcase the data forwarding concept. In real-world scenarios, you would need to handle data validation, implement security measures, and consider the architecture and structure of the receiving site according to your specific requirements.


