// server.js
const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');
const app = express();

// Replace with your secret key
const secretKey = '6LelJxAqAAAAAI0XQXVf8pYJbpPHKhjHR2J6PgUU';

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.post('/', async (req, res) => {
  const token = req.body['g-recaptcha-response'];

  if (!token) {
    return res.json({ success: false, message: 'No token provided' });
  }

  const verifyUrl = `https://www.google.com/recaptcha/api/siteverify?secret=${secretKey}&response=${token}`;

  try {
    const response = await axios.post(verifyUrl);
    const { success } = response.data;

    if (!success) {
      return res.json({ success: false, message: 'Failed captcha verification' });
    }

    return res.json({ success: true, message: 'Captcha passed' });
  } catch (error) {
    return res.json({ success: false, message: 'Error verifying captcha' });
  }
});

app.listen(3000, () => {
  console.log('Server started on http://127.0.0.1:3000');
});
