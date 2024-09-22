#!/usr/bin/env python3

import sys
import dns.resolver
from termcolor import colored


def query_mx_record(domain):
    """Query the MX record of the domain."""
    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        print(colored(f"[✓] MX record found for {domain}", "green"))
        for mx in mx_records:
            print(f"  - {mx.exchange} (Priority: {mx.preference})")
    except dns.resolver.NoAnswer:
        print(colored(f"[✗] No MX record found for {domain}.", "red"))
        print("  Recommendation: Configure MX records to handle emails properly.")
    except Exception as e:
        print(colored(f"[✗] Error fetching MX record for {domain}: {e}", "red"))


def query_spf_record(domain):
    """Query the SPF record of the domain."""
    try:
        txt_records = dns.resolver.resolve(domain, 'TXT')
        for txt in txt_records:
            if "v=spf1" in str(txt):
                print(colored(f"[✓] SPF record found for {domain}: {txt}", "green"))
                return
        print(colored(f"[✗] No valid SPF record found for {domain}.", "red"))
        print("  Recommendation: Configure SPF to prevent email spoofing (e.g., 'v=spf1 include:_spf.yourdomain.com').")
    except dns.resolver.NoAnswer:
        print(colored(f"[✗] No SPF record found for {domain}.", "red"))
        print("  Recommendation: Configure SPF to prevent email spoofing.")
    except Exception as e:
        print(colored(f"[✗] Error fetching SPF record for {domain}: {e}", "red"))


def query_dkim_record(domain):
    """Query the DKIM record of the domain."""
    dkim_selector = "default"  # Common selector used, can be adjusted per domain.
    try:
        dkim_domain = f"{dkim_selector}._domainkey.{domain}"
        dkim_record = dns.resolver.resolve(dkim_domain, 'TXT')
        for txt in dkim_record:
            if "v=DKIM1" in str(txt):
                print(colored(f"[✓] DKIM record found for {dkim_domain}: {txt}", "green"))
                return
        print(colored(f"[✗] No valid DKIM record found for {dkim_domain}.", "red"))
        print(f"  Recommendation: Configure DKIM with a selector like '{dkim_selector}' for signing emails.")
    except dns.resolver.NoAnswer:
        print(colored(f"[✗] No DKIM record found for {dkim_domain}.", "red"))
        print(f"  Recommendation: Configure DKIM for signing outgoing emails.")
    except Exception as e:
        print(colored(f"[✗] Error fetching DKIM record for {dkim_domain}: {e}", "red"))


def query_dmarc_record(domain):
    """Query the DMARC record of the domain."""
    try:
        dmarc_domain = f"_dmarc.{domain}"
        dmarc_record = dns.resolver.resolve(dmarc_domain, 'TXT')
        for txt in dmarc_record:
            if "v=DMARC1" in str(txt):
                print(colored(f"[✓] DMARC record found for {dmarc_domain}: {txt}", "green"))
                return
        print(colored(f"[✗] No valid DMARC record found for {dmarc_domain}.", "red"))
        print(
            "  Recommendation: Configure DMARC to specify how emails from your domain should be handled by receiving mail servers.")
    except dns.resolver.NoAnswer:
        print(colored(f"[✗] No DMARC record found for {dmarc_domain}.", "red"))
        print("  Recommendation: Configure DMARC for domain protection.")
    except Exception as e:
        print(colored(f"[✗] Error fetching DMARC record for {dmarc_domain}: {e}", "red"))


def main():
    """Main function to run the email security check."""
    if len(sys.argv) != 2:
        print("Usage: ./email_security_check.py <domain>")
        sys.exit(1)

    domain = sys.argv[1]

    print(f"Checking email security for domain: {domain}\n")

    # Check MX records
    query_mx_record(domain)
    print("")

    # Check SPF record
    query_spf_record(domain)
    print("")

    # Check DKIM record
    query_dkim_record(domain)
    print("")

    # Check DMARC record
    query_dmarc_record(domain)
    print("")


if __name__ == "__main__":
    main()
