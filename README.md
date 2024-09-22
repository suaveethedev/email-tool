# Email Security Checker

```email_security_check.py``` is a Python-based tool to check the security posture of a domain's email service. It verifies the following DNS records for email security:

* **MX Records:** Ensures the domain can handle email.
* **SPF Records:** Helps prevent email spoofing.
* **DKIM Records:** Verifies the authenticity of the sender.
* **DMARC Records:** Enforces email handling policies.

## Prerequisites

### Dependencies
This tool requires the following Python packages:

* ```dnspython```: To query DNS records.
* ```termcolor```: For colored terminal output.

You can install the dependencies via pip:
```bash
pip install -r requirements.txt
```

### Installing ```dnspython``` and ```termcolor``` manually:
```bash
pip install dnspython termcolor
```

## Usage
To run the email security check, execute the script as follows:
```bash
./email_security_check.py <domain>
```

### Example:
```bash
./email_security_check.py example.com
```
This command will check the following records for `example.com`:

1. **MX Record:** Mail exchange records to verify if the domain can receive emails.
2. **SPF Record:** Checks the presence of an SPF record to prevent email spoofing.
3. **DKIM Record:** Looks for DKIM records for email authenticity.
4. **DMARC Record:** Ensures that DMARC policies are set up for email protection.

## Output
For each type of record, the tool will output either a success or failure message, along with recommendations if records are missing or incorrect.

### Sample Output
```
Checking email security for domain: example.com

[✓] MX record found for example.com
  - mx1.example.com. (Priority: 10)

[✓] SPF record found for example.com: "v=spf1 include:_spf.example.com -all"

[✗] No valid DKIM record found for default._domainkey.example.com.
  Recommendation: Configure DKIM with a selector like 'default' for signing emails.

[✓] DMARC record found for _dmarc.example.com: "v=DMARC1; p=none"
```

## Recommendations
* **MX Records:** Make sure your domain has valid MX records to handle incoming emails.
* **SPF Records:** Use SPF records to prevent unauthorized users from sending emails on behalf of your domain.
* **DKIM Records:** Implement DKIM with proper selectors to sign your outgoing emails and ensure authenticity.
* **DMARC Records:** Set up DMARC to dictate how email servers should handle messages that fail SPF or DKIM checks.

## Contributing
If you find issues or have ideas for improvements, feel free to open an issue or submit a pull request!

