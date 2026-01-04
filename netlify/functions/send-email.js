// Netlify Function to send emails via SendGrid
exports.handler = async (event) => {
    // Only allow POST
    if (event.httpMethod !== 'POST') {
        return {
            statusCode: 405,
            body: JSON.stringify({ error: 'Method not allowed' })
        };
    }

    // Parse request body
    let body;
    try {
        body = JSON.parse(event.body);
    } catch (e) {
        return {
            statusCode: 400,
            body: JSON.stringify({ error: 'Invalid JSON body' })
        };
    }

    const { email, packName, source } = body;

    if (!email) {
        return {
            statusCode: 400,
            body: JSON.stringify({ error: 'Email is required' })
        };
    }

    // Get env vars
    const SENDGRID_API_KEY = process.env.SENDGRID_API_KEY;
    const SENDGRID_FROM_EMAIL = process.env.SENDGRID_FROM_EMAIL;

    if (!SENDGRID_API_KEY || !SENDGRID_FROM_EMAIL) {
        console.error('SendGrid environment variables not configured');
        return {
            statusCode: 500,
            body: JSON.stringify({ error: 'Email service not configured' })
        };
    }

    // Prepare email content
    const emailContent = {
        personalizations: [{
            to: [{ email: 'muffs@proteinmuffins.com' }]
        }],
        from: { email: SENDGRID_FROM_EMAIL },
        subject: `New Signup: ${packName || 'Recipe Pack'}`,
        content: [{
            type: 'text/plain',
            value: `New email signup!\n\nEmail: ${email}\nPack: ${packName || 'Not specified'}\nSource: ${source || 'Not specified'}\nTime: ${new Date().toISOString()}`
        }]
    };

    try {
        const response = await fetch('https://api.sendgrid.com/v3/mail/send', {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${SENDGRID_API_KEY}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(emailContent)
        });

        if (!response.ok) {
            const errorText = await response.text();
            console.error('SendGrid error:', errorText);
            return {
                statusCode: response.status,
                body: JSON.stringify({ error: 'Failed to send email' })
            };
        }

        return {
            statusCode: 200,
            body: JSON.stringify({ success: true, message: 'Email sent successfully' })
        };
    } catch (error) {
        console.error('SendGrid request failed:', error);
        return {
            statusCode: 500,
            body: JSON.stringify({ error: 'Failed to send email' })
        };
    }
};
