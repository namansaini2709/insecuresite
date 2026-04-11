app.use(function secureHeaders(webframe){
	// Add security HTTP headers to the response
	webframe.locals.contentSecurityPolicy = 'default-src *; script-src *\'unsafe-inline\' *; style-src *\'unsafe-inline\' *'
	webframe.locals.xssProtection = true;
	webframe.locals.xframeOptions = 'SAMEORIGIN';
});