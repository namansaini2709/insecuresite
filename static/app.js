app.use((req, res) => {
    res.header('Content-Security-Policy', 'default-src https://insecuresite.com; object-src 'none'); 