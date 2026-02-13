# Contact Form Backend Integration Guide

The contact form is now ready to be connected to a backend. Here are three options:

## Option 1: Formspree (Easiest - Recommended for Quick Setup)

**No backend required!** Formspree handles form submissions and sends emails.

### Setup Steps:
1. Go to https://formspree.io/ and sign up (free tier available)
2. Create a new form
3. Copy your form ID (looks like: `abc123xyz`)
4. In `index.html`, find line ~800 and replace `YOUR_FORMSPREE_ID` with your actual form ID:
   ```javascript
   const formspreeEndpoint = 'https://formspree.io/f/YOUR_FORMSPREE_ID';
   ```
5. Done! The form will now send emails to your specified address.

**Free tier:** 50 submissions/month

---

## Option 2: Custom Backend Endpoint

If you have your own backend API.

### Setup Steps:
1. In `index.html`, find the commented section for "OPTION 2: Custom Backend Endpoint" (around line ~830)
2. Uncomment that code block
3. Replace `https://your-backend.com/api/contact` with your actual endpoint
4. Make sure your backend accepts POST requests with JSON body:
   ```json
   {
     "name": "John Doe",
     "email": "john@example.com",
     "subject": "Hello",
     "message": "Message text"
   }
   ```
5. Your backend should return a 200 status code on success

### Example Backend (Node.js/Express):
```javascript
app.post('/api/contact', async (req, res) => {
  const { name, email, subject, message } = req.body;
  
  // Send email using nodemailer, sendgrid, etc.
  // Or save to database
  
  res.json({ success: true });
});
```

---

## Option 3: EmailJS (Client-side Email Sending)

Send emails directly from the browser without a backend.

### Setup Steps:
1. Sign up at https://www.emailjs.com/
2. Create an email service (Gmail, Outlook, etc.)
3. Create an email template
4. Get your Service ID and Template ID
5. In `index.html`, add EmailJS script before closing `</body>`:
   ```html
   <script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@3/dist/email.min.js"></script>
   <script>
     emailjs.init('YOUR_PUBLIC_KEY');
   </script>
   ```
6. Uncomment the "OPTION 3: EmailJS" section in the form handler
7. Replace `YOUR_SERVICE_ID` and `YOUR_TEMPLATE_ID` with your actual IDs

**Free tier:** 200 emails/month

---

## Current Status

The form is currently set up for **Formspree** (Option 1) but needs your Formspree ID to work.

To test without a backend, the form will show an error message. Once you add your Formspree ID, it will work immediately!

---

## Features Included

✅ Form validation (required fields)
✅ Loading state (button shows "Sending..." while processing)
✅ Success/error messages
✅ Form reset after successful submission
✅ Disabled button state during submission
✅ Smooth animations

---

## Need Help?

- Formspree Docs: https://help.formspree.io/
- EmailJS Docs: https://www.emailjs.com/docs/
- For custom backend, ensure CORS is enabled if hosting on a different domain
