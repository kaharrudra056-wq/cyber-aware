"""Run this to populate and update the database with comprehensive cybersecurity training data."""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app
from models import db
from models.user import User
from models.quiz import Topic, Question

app = create_app()

TOPICS = [
    # ========================================================
    # BASIC LEVEL (BEGINNER / FOUNDATIONAL CYBER HYGIENE)
    # ========================================================
    {
        'title': 'Password Security & Credential Hygiene',
        'slug': 'password-security',
        'icon': '🔑',
        'level': 'Basic',
        'order': 1,
        'description': 'Master strong password creation, entropy, password managers, and brute-force defenses.',
        'content': '''<h4>1. The Psychology and Mathematics of Passwords</h4>
<p>Passwords remain the primary barrier protecting your digital identity. Weak passwords or credential reuse across multiple services are responsible for over <strong>80% of data breaches</strong> globally. Attackers use automated tools like <em>John the Ripper</em> and <em>Hashcat</em> capable of testing billions of combinations per second on GPU rigs.</p>

<h4>2. Common Password Attacks</h4>
<ul>
  <li><strong>Brute-Force Attack:</strong> Automated software tries every possible character combination systematically.</li>
  <li><strong>Dictionary Attack:</strong> Uses lists of millions of common passwords, leaked databases (e.g., RockYou.txt), and common words.</li>
  <li><strong>Credential Stuffing:</strong> Attackers take username/password pairs stolen from one breach and test them automatically across hundreds of other websites.</li>
  <li><strong>Password Spraying:</strong> Attackers try a few common passwords (e.g., <em>Welcome@2024</em>) against thousands of user accounts to avoid account lockout policies.</li>
</ul>

<h4>3. Password Strength vs. Crack Time</h4>
<div class="table-responsive">
  <table class="table table-bordered table-striped">
    <thead class="table-dark">
      <tr><th>Password Pattern</th><th>Complexity</th><th>Estimated Crack Time (Modern GPU)</th><th>Verdict</th></tr>
    </thead>
    <tbody>
      <tr><td><code>password123</code></td><td>Numbers & lowercase (11 chars)</td><td>Instant (&lt; 1 second)</td><td>❌ Dangerously Weak</td></tr>
      <tr><td><code>john@1995</code></td><td>Names & common symbols (9 chars)</td><td>~2 minutes</td><td>❌ Very Weak</td></tr>
      <tr><td><code>Tr@7#kL92!xQ</code></td><td>Mixed uppercase, lowercase, numbers, symbols (12 chars)</td><td>~3,000 years</td><td>✅ Very Strong</td></tr>
      <tr><td><code>correct-horse-battery-staple</code></td><td>Multi-word passphrase (28 chars)</td><td>~100 million years</td><td>🛡️ Maximum Security</td></tr>
    </tbody>
  </table>
</div>

<h4>4. Golden Rules for Credential Hygiene</h4>
<ul>
  <li><strong>Length over Complexity:</strong> A 16-character passphrase is mathematically exponentially harder to crack than an 8-character complex password.</li>
  <li><strong>Never Reuse:</strong> Treat every website as potentially compromisable. Never share passwords between banking, personal email, and social media.</li>
  <li><strong>Use a Password Manager:</strong> Modern security consensus recommends using audited managers such as <strong>Bitwarden</strong>, <strong>1Password</strong>, or <strong>KeePassXC</strong>. You only remember one master passphrase; the manager handles 20+ character random strings for everything else.</li>
  <li><strong>Check for Leaks:</strong> Periodically check whether your email has appeared in public breaches using trusted databases such as <em>HaveIBeenPwned.com</em>.</li>
</ul>'''
    },
    {
        'title': 'Phishing, Smishing & Vishing Attacks',
        'slug': 'phishing',
        'icon': '🎣',
        'level': 'Basic',
        'order': 2,
        'description': 'Identify social engineering deception in emails, SMS messages, and voice calls.',
        'content': '''<h4>1. Understanding Phishing in Depth</h4>
<p>Phishing is a form of social engineering where an adversary impersonates a reputable entity (such as your bank, employer, Netflix, or government agency) to deceive you into disclosing sensitive information, clicking malicious payloads, or transferring funds. Over <strong>91% of cyber attacks</strong> commence with a phishing email.</p>

<h4>2. Types of Phishing Attacks</h4>
<ul>
  <li><strong>Mass Email Phishing:</strong> Generalized fraudulent emails sent to millions simultaneously (e.g., "Your PayPal account has been suspended").</li>
  <li><strong>Spear Phishing:</strong> Highly targeted, customized attacks aimed at a specific individual or organization using researched personal information.</li>
  <li><strong>Whaling:</strong> Spear phishing specifically targeting C-level executives (CEOs, CFOs) for high-value wire transfers.</li>
  <li><strong>Smishing (SMS Phishing):</strong> Fraudulent text messages claiming package delivery issues or bank account freezes with a short URL.</li>
  <li><strong>Vishing (Voice Phishing):</strong> Phone calls where attackers pretend to be tech support (Microsoft/Apple), police, or credit card fraud departments.</li>
  <li><strong>Clone Phishing:</strong> Attackers copy a legitimate, previously delivered email and swap out the attachment or link with a malicious version.</li>
</ul>

<h4>3. The 7 Major Red Flags 🚩</h4>
<ol>
  <li><strong>Artificial Urgency & Fear:</strong> Statements like <em>"Account suspended within 2 hours!"</em> or <em>"Arrest warrant issued"</em> designed to induce panic.</li>
  <li><strong>Mismatched Sender Domains:</strong> Display name says "Netflix Support", but the actual header reveals <code>support@net-flix-secure-pay.com</code>.</li>
  <li><strong>Generic Salutations:</strong> "Dear Customer" or "Valued Member" instead of your actual registered name.</li>
  <li><strong>Deceptive Hyperlinks:</strong> The visible text displays <code>https://mybank.com</code>, but hovering over the link reveals a destination to <code>http://192.168.1.55/login.php</code>.</li>
  <li><strong>Punycode / Homograph Attacks:</strong> Using Cyrillic or Unicode characters that visually mimic Latin letters (e.g., replacing Latin 'a' with Cyrillic 'а').</li>
  <li><strong>Unsolicited Attachments:</strong> Receiving unexpected `.zip`, `.exe`, `.scr`, or macro-enabled `.xlsm` files.</li>
  <li><strong>Requests for Sensitive Data:</strong> Legitimate banks and universities will never ask for your PIN, CVV, or passwords over email or phone.</li>
</ol>

<h4>4. What to Do If You Click a Phishing Link</h4>
<p>1. Immediately disconnect your device from the internet (unplug ethernet / turn off Wi-Fi).<br>
2. From a separate, clean device, change the passwords for any accounts potentially compromised.<br>
3. Enable Multi-Factor Authentication immediately.<br>
4. Run an exhaustive antivirus / antimalware scan on the impacted device.<br>
5. Report the incident to your institution's IT security team or the National Cyber Crime Portal (1930 in India).</p>'''
    },
    {
        'title': 'Safe Browsing & Web Security',
        'slug': 'safe-browsing',
        'icon': '🌐',
        'level': 'Basic',
        'order': 3,
        'description': 'Master HTTPS, certificates, privacy extensions, malicious downloads, and web privacy.',
        'content': '''<h4>1. The Mechanics of Web Security</h4>
<p>Browsing the web exposes your workstation to multiple threat vectors, including malicious scripts, cookie theft, unencrypted transport interception, and tracking beacons. Understanding web protocols is critical for personal privacy and organizational security.</p>

<h4>2. HTTP vs. HTTPS (SSL/TLS Encryption)</h4>
<p><strong>HTTP (Hypertext Transfer Protocol):</strong> Data is transmitted across networks in plain text. Any intermediary (ISP, coffee shop Wi-Fi operator, government wiretap) can inspect your passwords, messages, and session tokens via packet sniffing.</p>
<p><strong>HTTPS (HTTP Secure):</strong> Uses Transport Layer Security (TLS) to encrypt the bidirectional channel between your browser and the web server using public-key cryptography. It provides three essential guarantees:</p>
<ul>
  <li><strong>Confidentiality:</strong> Eavesdroppers cannot read your transmission.</li>
  <li><strong>Integrity:</strong> Attackers cannot tamper with or modify data in transit.</li>
  <li><strong>Authentication:</strong> Cryptographic certificates prove you are connected to the genuine host server, not an impostor.</li>
</ul>
<div class="alert alert-warning"><strong>Important Caution:</strong> HTTPS only guarantees that your connection to that specific server is encrypted — it does <em>not</em> guarantee the website itself is trustworthy. Cybercriminals routinely host phishing sites on HTTPS using free certificates!</div>

<h4>3. Modern Web Threats</h4>
<ul>
  <li><strong>Drive-by Downloads:</strong> Malicious web pages that automatically exploit browser vulnerabilities to install software without clicking anything.</li>
  <li><strong>Malvertising:</strong> Legitimate high-traffic news websites unknowingly displaying advertisement networks infected with exploit kits.</li>
  <li><strong>Browser Extension Hijacking:</strong> Harmless browser extensions bought by malicious developers who update them with background credential scrapers.</li>
  <li><strong>Clickjacking:</strong> Transparent UI layers overlaid on genuine buttons that trick you into clicking malicious links while intending to click a normal button.</li>
</ul>

<h4>4. Essential Browser Hardening Checklist</h4>
<ul>
  <li>Install an open-source content blocker such as <strong>uBlock Origin</strong> to block malicious scripts, tracking domains, and scam popups.</li>
  <li>Enable <strong>DNS over HTTPS (DoH)</strong> with providers like Cloudflare (1.1.1.1) or Quad9 (9.9.9.9) to prevent ISPs from logging domain visits.</li>
  <li>Regularly audit and remove unnecessary browser extensions.</li>
  <li>Never allow websites to save credit card information or primary passwords in unsecured browser caches.</li>
</ul>'''
    },

    # ========================================================
    # INTERMEDIATE LEVEL (SYSTEM & NETWORK DEFENSE)
    # ========================================================
    {
        'title': 'Malware, Ransomware & Spyware Defense',
        'slug': 'malware',
        'icon': '🦠',
        'level': 'Intermediate',
        'order': 4,
        'description': 'Understand malware variants, zero-day threats, ransomware lifecycles, and defense strategies.',
        'content': '''<h4>1. What is Malware?</h4>
<p>Malware (short for <em>Malicious Software</em>) encompasses any software program specifically designed to compromise confidentiality, integrity, or availability of a host computer or network. In 2023 alone, over <strong>5.4 billion malware attacks</strong> were recorded globally.</p>

<h4>2. Classification of Malicious Software</h4>
<div class="table-responsive">
  <table class="table table-bordered table-striped">
    <thead class="table-dark">
      <tr><th>Malware Family</th><th>Mechanism of Operation</th><th>Primary Objective</th><th>Real-World Example</th></tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Ransomware</strong></td>
        <td>Encrypts files using asymmetric ciphers (RSA-4096 / AES-256) and demands cryptocurrency ransom for private keys.</td>
        <td>Financial extortion; double extortion threatens data leak if unpaid.</td>
        <td>WannaCry, LockBit, BlackCat</td>
      </tr>
      <tr>
        <td><strong>Spyware / Keyloggers</strong></td>
        <td>Runs silently in background, capturing keystrokes, clipboard data, webcam feeds, and login credentials.</td>
        <td>Espionage, identity theft, financial account takeover.</td>
        <td>Pegasus, AgentTesla, RedLine Stealer</td>
      </tr>
      <tr>
        <td><strong>Trojan Horses</strong></td>
        <td>Disguised as legitimate, useful software (e.g. cracked game, PDF converter) but delivers hidden backdoor payloads.</td>
        <td>Remote code execution, botnet recruitment, backdoor access.</td>
        <td>Emotet, Zeus, TrickBot</td>
      </tr>
      <tr>
        <td><strong>Worms</strong></td>
        <td>Self-replicating standalone programs that spread across computer networks by exploiting unpatched OS vulnerabilities without human intervention.</td>
        <td>Network saturation, automated payload propagation.</td>
        <td>Stuxnet, Conficker, SQL Slammer</td>
      </tr>
      <tr>
        <td><strong>Rootkits</strong></td>
        <td>Injects into the operating system kernel or bootloader, actively concealing its presence from task managers and antivirus scanners.</td>
        <td>Persistent undetected administrative control.</td>
        <td>Necurs, ZeroAccess</td>
      </tr>
    </tbody>
  </table>
</div>

<h4>3. The Ransomware Lifecycle</h4>
<p><strong>Initial Access:</strong> Phishing email attachment, vulnerable RDP (Remote Desktop) port, or drive-by download.<br>
<strong>Lateral Movement:</strong> Attacker scans local network, escalates privileges (e.g., abusing Active Directory), and locates sensitive databases.<br>
<strong>Data Exfiltration:</strong> Sensitive files are stolen prior to encryption for double extortion.<br>
<strong>Payload Execution:</strong> Volume Shadow Copies are deleted, and AES/RSA encryption routines are executed across local and network drives.<br>
<strong>Ransom Demand:</strong> Desktop wallpaper replaced with countdown timer and Tor payment instructions.</p>

<h4>4. The 3-2-1 Backup Rule (The Ultimate Ransomware Antidote)</h4>
<ul>
  <li>Maintain at least <strong>3 copies</strong> of your critical data.</li>
  <li>Store backups on <strong>2 different media types</strong> (e.g., local external SSD + cloud storage).</li>
  <li>Keep at least <strong>1 copy completely off-site / immutable</strong> (disconnected from network so ransomware cannot encrypt it).</li>
</ul>'''
    },
    {
        'title': 'Multi-Factor Authentication (MFA / 2FA)',
        'slug': '2fa',
        'icon': '🔐',
        'level': 'Intermediate',
        'order': 5,
        'description': 'Explore authentication factors, TOTP apps, security keys, and defenses against SIM swapping.',
        'content': '''<h4>1. What is Multi-Factor Authentication?</h4>
<p>Authentication verifies whether you are who you claim to be. Multi-Factor Authentication (MFA) requires proof from at least two distinct, independent categories of evidence before granting access. Even if an attacker steals your password, they cannot gain entry without the second factor.</p>

<h4>2. The Three Fundamental Authentication Factors</h4>
<ul>
  <li><strong>Knowledge Factor (Something You Know):</strong> Passwords, PINs, security question answers.</li>
  <li><strong>Possession Factor (Something You Have):</strong> Smartphone, Authenticator app, Hardware security key, Smart card.</li>
  <li><strong>Inherence Factor (Something You Are):</strong> Biometrics such as fingerprint, facial geometry, retina scan, or voiceprint.</li>
</ul>

<h4>3. The 2FA Security Hierarchy</h4>
<div class="table-responsive">
  <table class="table table-bordered table-striped">
    <thead class="table-dark">
      <tr><th>Mechanism</th><th>Security Level</th><th>Vulnerability / Risk</th><th>Recommendation</th></tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Hardware Keys (FIDO2 / WebAuthn)</strong><br>e.g. YubiKey</td>
        <td>🛡️ Maximum (Immune to Phishing)</td>
        <td>Physical loss of token (mitigated by having a backup key)</td>
        <td>Best for high-value accounts (Email, Banking, Cloud)</td>
      </tr>
      <tr>
        <td><strong>Authenticator Apps (TOTP)</strong><br>e.g. Google Authenticator, Bitwarden</td>
        <td>🔒 High Security</td>
        <td>Device theft or malware on phone</td>
        <td>Strongly recommended for all daily accounts</td>
      </tr>
      <tr>
        <td><strong>SMS / Voice OTP</strong></td>
        <td>⚠️ Moderate to Low</td>
        <td><strong>SIM Swapping</strong>, SS7 network interception, credential phishing</td>
        <td>Better than password alone, but upgrade to TOTP when possible</td>
      </tr>
      <tr>
        <td><strong>Email OTP</strong></td>
        <td>⚠️ Moderate</td>
        <td>If your email account is breached, all 2FA tokens are compromised</td>
        <td>Acceptable fallback only</td>
      </tr>
    </tbody>
  </table>
</div>

<h4>4. What is a SIM Swap Attack?</h4>
<p>In a SIM swap scam, a fraudster impersonates you, contacts your mobile telecom carrier, and convinces them to transfer your mobile phone number to a new SIM card under their control. Once completed, all your SMS-based 2FA one-time passwords route directly to the criminal's phone. <em>Defense: Never rely solely on SMS OTP for financial and master email accounts.</em></p>'''
    },
    {
        'title': 'Public Wi-Fi & Network Security',
        'slug': 'public-wifi',
        'icon': '📶',
        'level': 'Intermediate',
        'order': 6,
        'description': 'Protect your data on open networks, prevent Man-in-the-Middle attacks, and understand VPN tunnels.',
        'content': '''<h4>1. The Perils of Open Public Wi-Fi</h4>
<p>Airports, cafes, hotels, and college campuses offer free Wi-Fi for convenience, but public wireless networks are inherently insecure broadcast mediums. Anyone within radio frequency range running packet capture software (such as <em>Wireshark</em>) can potentially capture, inspect, and manipulate unencrypted wireless frames.</p>

<h4>2. Critical Public Wi-Fi Attack Vectors</h4>
<ul>
  <li><strong>Man-in-the-Middle (MitM) Attacks:</strong> An attacker inserts themselves between your device and the router, intercepting or altering data packets in real time.</li>
  <li><strong>Evil Twin Hotspots:</strong> Attackers deploy a rogue wireless access point broadcasting the exact SSID of the venue (e.g. <code>Starbucks_Guest_WiFi</code>). When your device automatically connects, all your network traffic routes through the attacker's laptop.</li>
  <li><strong>Packet Sniffing:</strong> Capturing unencrypted credentials, session cookies, and browsing history broadcast across the shared radio frequency spectrum.</li>
  <li><strong>SSL Stripping:</strong> Attackers downgrade secure HTTPS connections to plain HTTP, allowing them to harvest login credentials in plain text.</li>
</ul>

<h4>3. How VPNs Neutralize Wi-Fi Threats</h4>
<p>A <strong>Virtual Private Network (VPN)</strong> encapsulates your device's traffic inside an encrypted tunnel (using protocols like WireGuard or OpenVPN with AES-256 or ChaCha20 encryption). Even if you connect to a hostile Evil Twin router, the operator only sees unintelligible encrypted ciphertext traveling to the VPN server.</p>

<h4>4. Safe Public Wi-Fi Protocol</h4>
<ul>
  <li>Always verify the exact network name and password with venue staff before connecting.</li>
  <li>Turn off "Auto-Connect to Open Wi-Fi Networks" on your laptop and smartphone.</li>
  <li>Keep your VPN connected continuously whenever on untrusted networks.</li>
  <li>Never execute financial banking transactions or login to sensitive admin accounts on open Wi-Fi.</li>
  <li>Turn off file sharing, AirDrop, and network printer discovery in OS settings.</li>
</ul>'''
    },
    {
        'title': 'Mobile Device Security & Endpoint Hardening',
        'slug': 'mobile-security',
        'icon': '📱',
        'level': 'Intermediate',
        'order': 7,
        'description': 'Secure smartphones, app permissions, prevent juice jacking, and defend against zero-click mobile spyware.',
        'content': '''<h4>1. Mobile Devices as Primary Attack Targets</h4>
<p>Smartphones contain our most sensitive personal information: banking apps, private conversations, location telemetry, biometric data, and active session tokens. As a result, mobile platforms (Android and iOS) have become prime targets for state-sponsored spyware and commercial malware syndicates.</p>

<h4>2. Major Mobile Threat Vectors</h4>
<ul>
  <li><strong>Sideloading & Malicious APKs:</strong> Installing applications from third-party websites or forums bypasses Google Play Protect and Apple App Store verification, frequently introducing trojanized spyware.</li>
  <li><strong>Over-Privileged Applications:</strong> Harmless-looking apps (e.g. calculators, flashlight apps) requesting invasive permissions such as Contacts, Microphone, SMS, and Background Location.</li>
  <li><strong>Juice Jacking:</strong> Public USB charging kiosks modified by attackers to extract data or deliver malware payloads through physical USB data pins while your phone is plugged in to charge.</li>
  <li><strong>Zero-Click Exploits:</strong> Advanced surveillance malware (e.g. NSO Group's <em>Pegasus</em>) that compromises a device via an incoming message or call without the user ever tapping or clicking anything.</li>
  <li><strong>Outdated Mobile Operating Systems:</strong> Delaying OS security updates leaves known remote code execution vulnerabilities unpatched on your device.</li>
</ul>

<h4>3. Mobile Hardening Best Practices</h4>
<ul>
  <li><strong>Lock Down Permissions:</strong> Regularly audit app permissions. Revoke Location, Camera, and Microphone access for all non-essential apps. Set location permissions to "Only while using app".</li>
  <li><strong>Enable Full-Disk Encryption:</strong> Ensure modern device encryption and use a 6+ digit alphanumeric passcode (avoid simple 4-digit PINs or pattern locks).</li>
  <li><strong>Use USB Data Blockers:</strong> When charging at airports or public stations, use a "USB data blocker" (a physical adapter that physically severs data pins, passing only electrical power).</li>
  <li><strong>Regular Reboots:</strong> Rebooting your smartphone daily flushes memory-resident, non-persistent spyware payloads from RAM.</li>
</ul>'''
    },

    # ========================================================
    # ADVANCED LEVEL (ENTERPRISE, APPLICATION & INFRASTRUCTURE)
    # ========================================================
    {
        'title': 'Social Engineering & Psychological Manipulation',
        'slug': 'social-engineering',
        'icon': '👤',
        'level': 'Advanced',
        'order': 8,
        'description': 'Deconstruct pretexting, authority bias, baiting, OSINT reconnaissance, and human vulnerability defenses.',
        'content': '''<h4>1. The Art of Human Hacking</h4>
<p>Renowned security consultant Kevin Mitnick famously stated: <em>"The human factor is truly that weakest link in security."</em> Social engineering bypasses cryptographic algorithms, next-generation firewalls, and biometric access controls by directly manipulating human psychology, trust, and cognitive biases.</p>

<h4>2. Psychological Principles Exploited by Attackers</h4>
<ul>
  <li><strong>Authority:</strong> Impersonating corporate executives (CEO fraud), law enforcement officers, or senior IT directors to induce compliance.</li>
  <li><strong>Urgency & Scarcity:</strong> Manufacturing high-stress deadlines (<em>"Wire funds within 30 minutes to close this acquisition"</em>) that disrupt logical critical reasoning.</li>
  <li><strong>Social Proof / Consensus:</strong> Convincing the victim that others in their department have already approved the request.</li>
  <li><strong>Likability & Flattery:</strong> Building rapport and sympathy to lower the victim's natural defensive suspicion.</li>
</ul>

<h4>3. Common Social Engineering Vectors</h4>
<div class="table-responsive">
  <table class="table table-bordered table-striped">
    <thead class="table-dark">
      <tr><th>Vector</th><th>Technique</th><th>Scenario</th></tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Pretexting</strong></td>
        <td>Creating an intricate, researched backstory to justify requesting confidential data.</td>
        <td>Attacker calls HR pretending to be an auditor needing employee payroll records for tax compliance.</td>
      </tr>
      <tr>
        <td><strong>Baiting</strong></td>
        <td>Enticing victims with a physical or digital prize containing a hidden malicious payload.</td>
        <td>Leaving infected USB flash drives labeled "Executive Salaries 2024" in the corporate parking lot.</td>
      </tr>
      <tr>
        <td><strong>Tailgating / Piggybacking</strong></td>
        <td>Physically following an authorized employee into a secured physical facility.</td>
        <td>Attacker holding heavy coffee boxes asking an employee to hold open the electronic keycard door.</td>
      </tr>
      <tr>
        <td><strong>Quid Pro Quo</strong></td>
        <td>Offering a helpful service in exchange for confidential information or access.</td>
        <td>Attacker calls employees claiming to be IT support helping fix an internet slowdown if they supply login credentials.</td>
      </tr>
    </tbody>
  </table>
</div>

<h4>4. Institutional Defense: The STOP Protocol</h4>
<p>Whenever you receive an unexpected request for money, access, or private credentials:</p>
<ol>
  <li><strong>S - Slow Down:</strong> Fraud thrives on urgency. Refuse to be rushed.</li>
  <li><strong>T - Think:</strong> Does this request make logical sense? Why does this person need this information?</li>
  <li><strong>O - Out-of-Band Verify:</strong> Call the requester on a known, official telephone number — never use numbers provided in the suspicious message.</li>
  <li><strong>P - Protect:</strong> Report the incident to information security officers immediately.</li>
</ol>'''
    },
    {
        'title': 'Network Defense, Firewalls & Intrusion Detection',
        'slug': 'network-defense',
        'icon': '🛡️',
        'level': 'Advanced',
        'order': 9,
        'description': 'Master packet filtering, stateful firewalls, IDS/IPS architectures, DMZ segmentation, and DDoS mitigation.',
        'content': '''<h4>1. Fundamentals of Enterprise Network Defense</h4>
<p>Network security is the practice of securing computer networks against unauthorized access, malicious modification, and resource depletion. A robust security posture implements <strong>Defense-in-Depth</strong>, layering controls across the physical, data link, network, transport, and application layers of the OSI model.</p>

<h4>2. Firewall Architectures</h4>
<ul>
  <li><strong>Stateless Packet Filtering (Layer 3/4):</strong> Evaluates individual packets in isolation based on source/destination IP, port numbers, and protocol headers. Cannot detect attacks hidden within valid connections.</li>
  <li><strong>Stateful Inspection Firewalls:</strong> Tracks the ongoing state of active TCP/UDP connections. Packets are verified against state tables; incoming traffic is dropped unless it corresponds to an established internal outbound request.</li>
  <li><strong>Next-Generation Firewalls (NGFW / Layer 7):</strong> Performs deep packet inspection (DPI), application awareness, TLS decryption, and integrated threat intelligence to block advanced application-layer attacks.</li>
  <li><strong>Web Application Firewalls (WAF):</strong> Sits in front of web servers to inspect HTTP/HTTPS traffic, filtering SQL injection, XSS, and automated bot scrapers.</li>
</ul>

<h4>3. Intrusion Detection (IDS) vs. Intrusion Prevention (IPS)</h4>
<div class="table-responsive">
  <table class="table table-bordered table-striped">
    <thead class="table-dark">
      <tr><th>Capability</th><th>Intrusion Detection System (IDS)</th><th>Intrusion Prevention System (IPS)</th></tr>
    </thead>
    <tbody>
      <tr><td><strong>Network Placement</strong></td><td>Passive / Out-of-band (receives mirrored SPAN port traffic)</td><td>In-line (traffic flows directly through the sensor)</td></tr>
      <tr><td><strong>Action on Threat</strong></td><td>Generates real-time alerts and logs alerts to SIEM</td><td>Actively drops malicious packets, resets connections, and updates firewall rules</td></tr>
      <tr><td><strong>Network Latency</strong></td><td>Zero latency impact on active traffic</td><td>Can introduce minimal latency under high traffic loads</td></tr>
      <tr><td><strong>Analysis Methods</strong></td><td>Signature-based matching & Anomaly-based statistical heuristics</td><td>Signature matching, protocol anomaly checks & threat blocking</td></tr>
    </tbody>
  </table>
</div>

<h4>4. Demilitarized Zones (DMZ) & Network Segmentation</h4>
<p>A <strong>DMZ (Demilitarized Zone)</strong> is a perimeter network that isolates an organization's public-facing servers (Web, Mail, DNS) from the internal corporate LAN. If an internet-facing web server in the DMZ is compromised, the internal firewall prevents the attacker from laterally pivoting into internal workstations and core database servers.</p>'''
    },
    {
        'title': 'Web Application Security & OWASP Top 10',
        'slug': 'web-security',
        'icon': '💻',
        'level': 'Advanced',
        'order': 10,
        'description': 'Analyze injection vectors (SQLi), Cross-Site Scripting (XSS), CSRF, and defensive secure coding patterns.',
        'content': '''<h4>1. The Web Application Threat Landscape</h4>
<p>Web applications interface directly with the public internet, exposing business logic and backend datastores to untrusted inputs. The <strong>OWASP (Open Web Application Security Project) Top 10</strong> documents the most critical security risks facing modern web software.</p>

<h4>2. Critical Web Vulnerabilities</h4>
<ul>
  <li><strong>SQL Injection (SQLi):</strong> Occurs when untrusted user input is directly concatenated into database queries. Attackers can bypass authentication, exfiltrate entire databases, or delete data.<br>
  <em>Defense:</em> Always use parameterized queries / Object-Relational Mappers (ORM) such as SQLAlchemy and prepared statements. Never format strings into SQL.</li>
  <li><strong>Cross-Site Scripting (XSS):</strong>
    <ul>
      <li><em>Stored XSS:</em> Malicious scripts permanently saved in a database and served to other users.</li>
      <li><em>Reflected XSS:</em> Malicious script reflected off a web server in an error message or search result.</li>
      <li><em>DOM-Based XSS:</em> Vulnerability in client-side JavaScript executing untrusted DOM input.</li>
    </ul>
    <em>Defense:</em> Context-aware output encoding, automated Jinja2 template escaping, and Content Security Policy (CSP) headers.</li>
  <li><strong>Cross-Site Request Forgery (CSRF):</strong> Tricks an authenticated victim into executing unwanted state-changing actions (password change, fund transfer) on a trusted application.<br>
  <em>Defense:</em> Anti-CSRF synchronizer tokens and <code>SameSite=Lax</code> or <code>Strict</code> cookie attributes.</li>
  <li><strong>Broken Object Level Authorization (BOLA / IDOR):</strong> Applications exposing direct references to internal objects (e.g. <code>/api/invoices/1042</code>) without verifying if the requesting user owns that object.<br>
  <em>Defense:</em> Enforce strict server-side authorization checks on every object lookup.</li>
</ul>

<h4>3. Defensive Security Headers</h4>
<p>Modern web servers protect users by sending security directives in HTTP response headers:</p>
<ul>
  <li><code>Content-Security-Policy (CSP):</code> Restricts domains from which scripts, images, and styles can load.</li>
  <li><code>Strict-Transport-Security (HSTS):</code> Enforces all browser connections to use HTTPS exclusively.</li>
  <li><code>X-Content-Type-Options: nosniff:</code> Prevents MIME-type confusion attacks.</li>
  <li><code>X-Frame-Options: DENY:</code> Prevents clickjacking attacks by blocking iframe embedding.</li>
</ul>'''
    }
]

QUESTIONS = [
    # ========================================================
    # BASIC LEVEL QUESTIONS
    # ========================================================
    # Topic 1: Password Security (5 Questions)
    {'topic_slug': 'password-security', 'question_text': 'Which of the following password patterns offers the greatest resistance against modern GPU brute-force attacks?', 'option_a': 'password2024!', 'option_b': 'Admin@1234', 'option_c': 'solar-bicycle-ocean-granite', 'option_d': 'P@ssw0rd', 'correct_answer': 'C', 'explanation': 'Multi-word passphrases (e.g. "solar-bicycle-ocean-granite") have high length and high character entropy, requiring millions of years to crack with brute-force tools.'},
    {'topic_slug': 'password-security', 'question_text': 'What is the primary danger of reusing the same password across multiple online accounts?', 'option_a': 'It slows down your internet connection', 'option_b': 'If one website suffers a data breach, attackers use "Credential Stuffing" to compromise all your other accounts', 'option_c': 'Password managers refuse to save duplicate passwords', 'option_d': 'Web browsers automatically delete duplicate passwords', 'correct_answer': 'B', 'explanation': 'Credential stuffing attacks use stolen credentials from one breached website to automatically unlock accounts across hundreds of other popular platforms.'},
    {'topic_slug': 'password-security', 'question_text': 'What is the minimum password length recommended by modern cybersecurity standards (such as NIST)?', 'option_a': '6 characters', 'option_b': '8 characters', 'option_c': '12 to 16 characters', 'option_d': '32 characters', 'correct_answer': 'C', 'explanation': 'Modern standards recommend at least 12 to 16 characters because each additional character exponentially increases the computational work required to brute-force.'},
    {'topic_slug': 'password-security', 'question_text': 'Why is an open-source password manager (like Bitwarden or KeePassXC) safer than saving passwords in a browser?', 'option_a': 'Password managers encrypt the database with AES-256 and require zero knowledge master keys, protecting against local malware extraction', 'option_b': 'Password managers are managed by the government', 'option_c': 'Browsers do not encrypt passwords at all', 'option_d': 'Password managers only work on Linux operating systems', 'correct_answer': 'A', 'explanation': 'Audited password managers utilize client-side zero-knowledge AES-256 encryption with Argon2 or PBKDF2 key derivation, whereas browser vaults are frequently targeted by infostealers.'},
    {'topic_slug': 'password-security', 'question_text': 'What is "Password Spraying"?', 'option_a': 'Typing passwords very quickly to confuse keyloggers', 'option_b': 'Trying a single commonly used password against thousands of different user accounts to avoid account lockout triggers', 'option_c': 'Printing out passwords on paper', 'option_d': 'Deleting passwords from memory caches', 'correct_answer': 'B', 'explanation': 'Password spraying circumvents account lockout thresholds by testing one or two common passwords (e.g. "Summer2024!") against thousands of usernames rather than brute-forcing one account.'},

    # Topic 2: Phishing (5 Questions)
    {'topic_slug': 'phishing', 'question_text': 'You receive an email claiming to be from your bank stating: "URGENT: Your debit card is blocked. Click here within 1 hour." What is the primary red flag?', 'option_a': 'The email is formatted in HTML', 'option_b': 'Artificial urgency and fear tactics designed to bypass rational thinking', 'option_c': 'The email was delivered in the morning', 'option_d': 'The message includes the bank logo', 'correct_answer': 'B', 'explanation': 'Urgency, deadlines, and threats of financial loss are psychological coercion techniques used to induce panic so the victim acts before verifying.'},
    {'topic_slug': 'phishing', 'question_text': 'How should you verify the true destination of a hyperlink in a suspicious email without clicking it?', 'option_a': 'Click the link on your mobile phone instead', 'option_b': 'Forward the email to all your colleagues', 'option_c': 'Hover your mouse cursor over the link to preview the actual destination URL in the status bar', 'option_d': 'Reply to the sender asking if the link is safe', 'correct_answer': 'C', 'explanation': 'Hovering reveals the real destination URL, which often exposes a deceptive or malicious third-party domain hidden behind friendly text.'},
    {'topic_slug': 'phishing', 'question_text': 'What is "Whaling" in cybersecurity?', 'option_a': 'Catching large amounts of spam in a honeypot', 'option_b': 'A spear phishing attack specifically targeted at high-profile executives like CEOs or CFOs to execute fraudulent wire transfers', 'option_c': 'Attacking naval communication networks', 'option_d': 'Deleting large database tables', 'correct_answer': 'B', 'explanation': 'Whaling targets high-profile corporate or government executives with customized lures to authorize multi-million dollar transfers or disclose sensitive intellectual property.'},
    {'topic_slug': 'phishing', 'question_text': 'What constitutes a "Smishing" attack?', 'option_a': 'A phishing attack executed via SMS text messages containing malicious links or phone numbers', 'option_b': 'Phishing through social media friend requests', 'option_c': 'Stealing hard drives from servers', 'option_d': 'Sending fraudulent physical postal mail', 'correct_answer': 'A', 'explanation': 'Smishing (SMS Phishing) delivers deceptive text messages pretending to be package deliveries, tax refunds, or banking alerts.'},
    {'topic_slug': 'phishing', 'question_text': 'What is the safest immediate action to take if you realize you entered credentials on a fraudulent phishing page?', 'option_a': 'Shut down your computer and wait 24 hours', 'option_b': 'Immediately change your password from another clean device and enable Multi-Factor Authentication (MFA)', 'option_c': 'Email the attacker asking them not to use your password', 'option_d': 'Delete your web browser application', 'correct_answer': 'B', 'explanation': 'Changing credentials immediately from a known safe device and enabling MFA locks out the attacker before they can utilize the harvested password.'},

    # Topic 3: Safe Browsing (5 Questions)
    {'topic_slug': 'safe-browsing', 'question_text': 'What does the padlock icon (HTTPS) in your browser address bar fundamentally guarantee?', 'option_a': 'The website is 100% legal, safe, and vetted by law enforcement', 'option_b': 'Data transmitted between your browser and that specific server is encrypted and protected from transit tampering', 'option_c': 'The website does not contain any malware or phishing forms', 'option_d': 'Your computer cannot be infected by any virus', 'correct_answer': 'B', 'explanation': 'HTTPS guarantees end-to-end transport encryption and integrity; it does NOT verify the intent of the website operator. Phishing sites frequently use HTTPS.'},
    {'topic_slug': 'safe-browsing', 'question_text': 'What is a "Drive-by Download"?', 'option_a': 'Downloading files while connected to car Wi-Fi', 'option_b': 'Malware that downloads and executes automatically simply by visiting an infected web page without user clicking or consent', 'option_c': 'Downloading large torrent files overnight', 'option_d': 'Software installed through authorized operating system updates', 'correct_answer': 'B', 'explanation': 'Drive-by downloads exploit unpatched browser or plugin vulnerabilities (zero-days) to drop payloads silently upon page rendering.'},
    {'topic_slug': 'safe-browsing', 'question_text': 'How does an open-source content blocker like uBlock Origin enhance your cybersecurity posture?', 'option_a': 'It blocks malvertising domains, tracking beacons, and coin-mining scripts before they execute in your browser', 'option_b': 'It cracks Wi-Fi passwords for you', 'option_c': 'It increases your internet bandwidth by 500%', 'option_d': 'It replaces your operating system firewall', 'correct_answer': 'A', 'explanation': 'Ad and tracker blockers neutralize malvertising vectors by preventing victim browsers from fetching untrusted JavaScript from malicious ad networks.'},
    {'topic_slug': 'safe-browsing', 'question_text': 'What is "DNS over HTTPS" (DoH)?', 'option_a': 'A protocol that encrypts domain name lookup queries inside HTTPS traffic, preventing local ISPs and Wi-Fi operators from eavesdropping on visited websites', 'option_b': 'A method for hosting websites without domain names', 'option_c': 'A type of computer virus that attacks DNS servers', 'option_d': 'An email encryption standard', 'correct_answer': 'A', 'explanation': 'DoH prevents intermediaries (including public Wi-Fi providers and ISPs) from logging your DNS requests and executing DNS spoofing / redirection attacks.'},
    {'topic_slug': 'safe-browsing', 'question_text': 'What is "Clickjacking"?', 'option_a': 'Stealing a physical mouse from an office', 'option_b': 'A deceptive technique where invisible or transparent UI layers trick users into clicking malicious buttons while intending to click something else', 'option_c': 'Clicking buttons very rapidly in a web form', 'option_d': 'Purchasing expired domain names', 'correct_answer': 'B', 'explanation': 'Clickjacking overlays an invisible iframe over a legitimate page, tricking users into performing actions (such as authorizing permissions or buying items) unintentionally.'},

    # ========================================================
    # INTERMEDIATE LEVEL QUESTIONS
    # ========================================================
    # Topic 4: Malware (5 Questions)
    {'topic_slug': 'malware', 'question_text': 'What defines "Ransomware" compared to other classifications of malicious software?', 'option_a': 'It displays pop-up advertisements to generate ad revenue', 'option_b': 'It encrypts user files with strong cryptographic ciphers and demands payment in cryptocurrency in exchange for the decryption key', 'option_c': 'It logs keystrokes to steal bank accounts', 'option_d': 'It only attacks mobile smartphones', 'correct_answer': 'B', 'explanation': 'Ransomware holds user data hostage through uncrackable encryption algorithms (AES/RSA) and extorts victims for cryptocurrency.'},
    {'topic_slug': 'malware', 'question_text': 'What is the "3-2-1 Backup Strategy" for total ransomware resilience?', 'option_a': 'Keep 3 files, backup every 2 days, for 1 year', 'option_b': '3 total copies of data, stored on 2 different media types, with at least 1 copy kept completely offsite or immutable/air-gapped', 'option_c': 'Save backups to 3 USB drives in the same room', 'option_d': 'Backup only the 3 largest folders on your computer', 'correct_answer': 'B', 'explanation': 'Having an immutable, offline copy guarantees you can restore your files without ever paying a criminal ransom if internal networks are encrypted.'},
    {'topic_slug': 'malware', 'question_text': 'How does a computer "Worm" differ fundamentally from a traditional computer "Virus"?', 'option_a': 'Worms only infect Apple macOS computers', 'option_b': 'Worms can self-replicate and spread autonomously across networks without requiring user action or host file attachment', 'option_c': 'Viruses do not cause any harm to computer hardware', 'option_d': 'Worms are always benign educational programs', 'correct_answer': 'B', 'explanation': 'A virus requires a host file and human interaction (running an executable) to spread. A worm exploits network vulnerabilities to propagate automatically.'},
    {'topic_slug': 'malware', 'question_text': 'What is a "Trojan Horse" in software security?', 'option_a': 'A hardware virus embedded in computer power cables', 'option_b': 'Malware disguised as legitimate or desirable software (such as a game or cracked utility) that hides malicious payloads', 'option_c': 'A secure operating system developed in Greece', 'option_d': 'An antivirus program that removes all files', 'correct_answer': 'B', 'explanation': 'Trojans mislead users regarding their true intent, delivering backdoors, spyware, or ransomware once installed under false pretenses.'},
    {'topic_slug': 'malware', 'question_text': 'Why are "Rootkits" considered among the most dangerous malware infections?', 'option_a': 'They operate at the kernel or bootloader level, hiding themselves from the operating system and standard security tools', 'option_b': 'They automatically delete the computer monitor drivers', 'option_c': 'They cannot be detected even if the hard drive is physically destroyed', 'option_d': 'They require 100 GB of free disk space to run', 'correct_answer': 'A', 'explanation': 'Rootkits subvert the operating system kernel itself, intercepting system calls to conceal their processes, files, and network connections from task managers.'},

    # Topic 5: 2FA (5 Questions)
    {'topic_slug': '2fa', 'question_text': 'Which of the following represents an "Inherence" authentication factor?', 'option_a': 'A 6-digit numeric PIN', 'option_b': 'A hardware YubiKey token', 'option_c': 'A fingerprint or facial recognition scan', 'option_d': 'Your mother\'s maiden name', 'correct_answer': 'C', 'explanation': 'The three factors are: Something you know (Knowledge), Something you have (Possession), and Something you are (Inherence/Biometrics). Biometrics represent inherence.'},
    {'topic_slug': '2fa', 'question_text': 'Why are Hardware Security Keys (FIDO2/WebAuthn) superior to SMS-based 2FA codes?', 'option_a': 'Hardware keys never require an internet connection and are mathematically immune to phishing and SIM swapping', 'option_b': 'Hardware keys automatically guess your password if you forget it', 'option_c': 'SMS codes are limited to only 4 digits', 'option_d': 'Hardware keys can be shared with up to 10 family members simultaneously', 'correct_answer': 'A', 'explanation': 'Hardware keys use cryptographic origin binding that prevents credential harvesting on phishing sites, and they do not rely on cellular networks vulnerable to SIM swapping.'},
    {'topic_slug': '2fa', 'question_text': 'In a "SIM Swap" attack, what action does the cybercriminal take?', 'option_a': 'They steal your physical smartphone from your pocket', 'option_b': 'They deceive your mobile network carrier into transferring your telephone number to a SIM card they control', 'option_c': 'They physically replace your phone battery with a listening device', 'option_d': 'They install a fake SIM card reader on an ATM', 'correct_answer': 'B', 'explanation': 'SIM swapping is social engineering directed at telecom providers to hijack the victim\'s phone number, allowing the attacker to intercept all SMS verification codes.'},
    {'topic_slug': '2fa', 'question_text': 'How do Time-Based One-Time Password (TOTP) apps (like Google Authenticator) work?', 'option_a': 'They send an SMS message to Google servers every 30 seconds', 'option_b': 'They compute a 6-digit code using a shared secret key and the current Unix timestamp via the HMAC-SHA1 algorithm', 'option_c': 'They take a screenshot of your screen and analyze it', 'option_d': 'They require continuous Bluetooth connection to your computer', 'correct_answer': 'B', 'explanation': 'TOTP algorithms (RFC 6238) combine the secret seed key with the current 30-second time window cryptographically without requiring any cellular network connectivity.'},
    {'topic_slug': '2fa', 'question_text': 'What is "MFA Fatigue" (Push Bombing)?', 'option_a': 'Getting tired from typing passwords', 'option_b': 'An attacker spamming a victim with dozens of MFA push notification requests until the frustrated victim taps "Approve"', 'option_c': 'A mobile phone running out of battery due to MFA apps', 'option_d': 'Forgetting your MFA backup codes', 'correct_answer': 'B', 'explanation': 'MFA fatigue attacks exploit human exhaustion and confusion by repeatedly sending approval prompts until the target accidentally or desperately accepts.'},

    # Topic 6: Public Wi-Fi (5 Questions)
    {'topic_slug': 'public-wifi', 'question_text': 'What is an "Evil Twin" Wi-Fi attack?', 'option_a': 'A duplicate Wi-Fi password written on a coffee shop chalkboard', 'option_b': 'A rogue wireless access point configured with the same SSID name as a legitimate venue to trick devices into connecting', 'option_c': 'Connecting two smartphones to the same Bluetooth speaker', 'option_d': 'A computer virus that duplicates itself onto two hard drives', 'correct_answer': 'B', 'explanation': 'An Evil Twin is a fraudulent Wi-Fi hotspot set up by an attacker mimicking a legitimate network name (e.g. "Airport_Free_WiFi") to intercept all connected user traffic.'},
    {'topic_slug': 'public-wifi', 'question_text': 'How does a Virtual Private Network (VPN) protect users connected to an untrusted public network?', 'option_a': 'It increases Wi-Fi signal strength through the walls', 'option_b': 'It encapsulates all device traffic inside an encrypted tunnel, rendering intercepted packets unreadable to local eavesdroppers', 'option_c': 'It prevents physical theft of your laptop computer', 'option_d': 'It blocks all incoming emails that contain attachments', 'correct_answer': 'B', 'explanation': 'A VPN creates an encrypted tunnel between your device and the VPN server, ensuring any packet sniffer on the local Wi-Fi network only sees unintelligible encrypted ciphertext.'},
    {'topic_slug': 'public-wifi', 'question_text': 'What is "SSL Stripping"?', 'option_a': 'Removing an SSL certificate from an expired domain', 'option_b': 'A Man-in-the-Middle attack that downgrades secure HTTPS connections to unencrypted HTTP to intercept credentials in plain text', 'option_c': 'Uninstalling antivirus software before running a game', 'option_d': 'Cleaning browser history and cache files', 'correct_answer': 'B', 'explanation': 'In an SSL stripping attack, an adversary intercepts HTTPS requests and serves unencrypted HTTP pages to the victim, capturing submitted passwords and cookies in plain text.'},
    {'topic_slug': 'public-wifi', 'question_text': 'Why should device file sharing and AirDrop be disabled on public Wi-Fi networks?', 'option_a': 'To prevent malicious actors on the shared subnet from probing open ports, injecting files, or harvesting hostnames', 'option_b': 'Because open networks charge per megabyte of shared files', 'option_c': 'To prevent the router from overheating', 'option_d': 'It is required by municipal laws', 'correct_answer': 'A', 'explanation': 'Open file sharing protocols (such as SMB or NetBIOS) expose internal directories and host configurations to everyone on the untrusted subnet.'},
    {'topic_slug': 'public-wifi', 'question_text': 'What security protocol is the modern standard for home and enterprise wireless network encryption?', 'option_a': 'WEP', 'option_b': 'WPA3', 'option_c': 'Telnet', 'option_d': 'FTP', 'correct_answer': 'B', 'explanation': 'WPA3 (Wi-Fi Protected Access 3) uses SAE (Simultaneous Authentication of Equals) to deliver robust encryption even when using simple passphrases.'},

    # Topic 7: Mobile Security (5 Questions)
    {'topic_slug': 'mobile-security', 'question_text': 'What is the primary cybersecurity danger of "sideloading" apps from third-party websites rather than official app stores?', 'option_a': 'Sideloaded apps always consume 100% of your device battery within 10 minutes', 'option_b': 'Third-party APK files bypass official malware screening and may contain embedded trojans, spyware, or adware', 'option_c': 'Sideloading requires purchasing a secondary SIM card', 'option_d': 'Sideloaded apps are permanently deleted every time the phone restarts', 'correct_answer': 'B', 'explanation': 'Official app stores screen apps for malicious code and policy violations. Downloading unofficial APKs from forums or websites exposes devices to trojanized payloads.'},
    {'topic_slug': 'mobile-security', 'question_text': 'What is "Juice Jacking"?', 'option_a': 'Drinking energy drinks while coding', 'option_b': 'A cyber attack where compromised public USB charging kiosks install malware or extract data through USB data pins', 'option_c': 'Overclocking a smartphone CPU to increase speed', 'option_d': 'Stealing a smartphone while it is plugged into a wall outlet', 'correct_answer': 'B', 'explanation': 'USB cables transfer both power and data. In a juice jacking attack, compromised charging ports abuse data pins to push malicious code or exfiltrate private files.'},
    {'topic_slug': 'mobile-security', 'question_text': 'Why should smartphone users regularly review and audit app permissions?', 'option_a': 'To ensure apps are using the maximum amount of cellular data possible', 'option_b': 'To prevent over-privileged apps from silently recording audio, accessing locations, or harvesting contacts without a functional need', 'option_c': 'To make sure all apps have access to your bank account details', 'option_d': 'To change the color theme of the mobile operating system', 'correct_answer': 'B', 'explanation': 'Many rogue or monetized apps request permissions far beyond their functional scope (e.g. a flashlight app requesting contacts and microphone access) to harvest and sell user data.'},
    {'topic_slug': 'mobile-security', 'question_text': 'How does regular smartphone restarting (rebooting) defend against advanced mobile spyware (like Pegasus)?', 'option_a': 'It permanently deletes all installed applications', 'option_b': 'It flushes volatile RAM memory, terminating non-persistent zero-click payloads that do not have persistence mechanisms', 'option_c': 'It changes your IMEI number', 'option_d': 'It doubles device storage capacity', 'correct_answer': 'B', 'explanation': 'Many state-of-the-art mobile surveillance payloads operate exclusively in volatile memory to evade forensics; rebooting forces the attacker to reinfect the device.'},
    {'topic_slug': 'mobile-security', 'question_text': 'What does "Remote Wipe" capability provide if a mobile device is physically stolen?', 'option_a': 'It causes the battery to short-circuit', 'option_b': 'It allows the owner to send a cloud command that cryptographically erases all personal data and factory resets the device', 'option_c': 'It records a video of the thief and posts it online', 'option_d': 'It calls emergency services automatically', 'correct_answer': 'B', 'explanation': 'Services like Apple Find My and Google Find My Device permit remote cryptographic wiping to prevent thieves from accessing sensitive banking and personal files.'},

    # ========================================================
    # ADVANCED LEVEL QUESTIONS
    # ========================================================
    # Topic 8: Social Engineering (5 Questions)
    {'topic_slug': 'social-engineering', 'question_text': 'What is "Pretexting" in social engineering?', 'option_a': 'Sending an automatic out-of-office email response', 'option_b': 'Fabricating an elaborate fictional scenario or persona to manipulate a target into disclosing confidential data', 'option_c': 'Writing text messages before sending them', 'option_d': 'Testing software before deployment', 'correct_answer': 'B', 'explanation': 'Pretexting establishes an authentic-sounding backstory (e.g. pretending to be an external auditor or IT technician) to disarm suspicion.'},
    {'topic_slug': 'social-engineering', 'question_text': 'What is "Baiting" in social engineering?', 'option_a': 'Posting provocative comments on social media forums', 'option_b': 'Leaving malware-infected USB drives in public locations hoping curious employees will plug them into work computers', 'option_c': 'Sending email newsletters', 'option_d': 'Conducting legal online interviews', 'correct_answer': 'B', 'explanation': 'Baiting leverages human curiosity or greed (e.g. a labeled USB drive promising payroll data or free software) to trick targets into executing malware.'},
    {'topic_slug': 'social-engineering', 'question_text': 'In the STOP protocol for institutional defense against fraud, what does the "O" represent?', 'option_a': 'Open all email attachments immediately', 'option_b': 'Out-of-Band Verification: contacting the purported requester through a verified, independent communication channel', 'option_c': 'Overlook minor security errors', 'option_d': 'Operate without IT permissions', 'correct_answer': 'B', 'explanation': 'Out-of-band verification ensures you authenticate requests by calling known telephone numbers rather than replying via the medium where the request arrived.'},
    {'topic_slug': 'social-engineering', 'question_text': 'What is "Tailgating" (or Piggybacking) in physical security?', 'option_a': 'Following an authorized person closely through a secure door or turnstile without scanning valid credentials', 'option_b': 'Hacking into someone\'s car computer', 'option_c': 'Installing spyware on laptop touchpads', 'option_d': 'Sitting behind someone in a cafe to read their screen', 'correct_answer': 'A', 'explanation': 'Tailgating exploits social politeness (such as holding open a door for someone carrying packages) to bypass badge readers and biometric physical locks.'},
    {'topic_slug': 'social-engineering', 'question_text': 'What is Open Source Intelligence (OSINT) and how do social engineers utilize it?', 'option_a': 'Free open-source software like Linux', 'option_b': 'Gathering publicly available intelligence (LinkedIn, corporate bios, social media) to craft hyper-targeted pretexting scenarios', 'option_c': 'Stealing government classified satellite imagery', 'option_d': 'Encrypting open-source code', 'correct_answer': 'B', 'explanation': 'Adversaries harvest organizational charts, project names, and employee hobbies from public platforms to make their fraudulent communication seem completely genuine.'},

    # Topic 9: Network Defense (5 Questions)
    {'topic_slug': 'network-defense', 'question_text': 'What is the primary operational distinction between a Stateless packet filter and a Stateful inspection firewall?', 'option_a': 'Stateless firewalls only operate on Wi-Fi networks', 'option_b': 'Stateless evaluates packets individually in isolation, whereas Stateful tracks active connection tables to ensure incoming packets belong to established sessions', 'option_c': 'Stateful firewalls require physical keys to unlock', 'option_d': 'Stateless firewalls are illegal under international telecommunication standards', 'correct_answer': 'B', 'explanation': 'Stateful inspection maintains connection state tables, automatically blocking unsolicited inbound traffic while allowing legitimate return traffic from outbound requests.'},
    {'topic_slug': 'network-defense', 'question_text': 'What is the key functional difference between an Intrusion Detection System (IDS) and an Intrusion Prevention System (IPS)?', 'option_a': 'An IDS monitors and alerts on suspicious traffic out-of-band, while an IPS sits in-line and actively blocks or drops malicious packets in real time', 'option_b': 'An IDS only detects viruses on USB flash drives', 'option_c': 'An IPS cannot block network traffic', 'option_d': 'An IDS is purely hardware while an IPS is purely software', 'correct_answer': 'A', 'explanation': 'An IDS is passive and alerts security teams (SPAN port), whereas an IPS sits directly in the traffic flow to terminate malicious TCP sessions and drop exploit packets.'},
    {'topic_slug': 'network-defense', 'question_text': 'What is the purpose of a Demilitarized Zone (DMZ) in enterprise network architecture?', 'option_a': 'To store decommissioned server hardware', 'option_b': 'To isolate public-facing internet servers (Web, Mail) from the internal private LAN, preventing lateral pivoting in case of breach', 'option_c': 'To bypass all firewall rules for faster gaming connections', 'option_d': 'To provide free Wi-Fi to campus visitors', 'correct_answer': 'B', 'explanation': 'A DMZ creates a segmented buffer zone; if an external web server is compromised, internal firewall policies block the attacker from reaching core databases and employee machines.'},
    {'topic_slug': 'network-defense', 'question_text': 'Which widely used open-source command-line tool allows network security professionals to perform port scanning and service discovery?', 'option_a': 'Wireshark', 'option_b': 'Nmap (Network Mapper)', 'option_c': 'VLC Media Player', 'option_d': 'Hashcat', 'correct_answer': 'B', 'explanation': 'Nmap is the definitive tool for discovering hosts, open listening ports, operating system fingerprints, and running services across a network.'},
    {'topic_slug': 'network-defense', 'question_text': 'What type of network attack floods a target server with millions of synchronized spoofed packets to exhaust its bandwidth and memory resources?', 'option_a': 'Man-in-the-Middle (MitM)', 'option_b': 'Distributed Denial of Service (DDoS)', 'option_c': 'Cross-Site Scripting (XSS)', 'option_d': 'Buffer Overflow', 'correct_answer': 'B', 'explanation': 'DDoS attacks weaponize botnets to saturate network bandwidth or server connection tables, rendering legitimate services inaccessible to valid users.'},

    # Topic 10: Web Application Security (5 Questions)
    {'topic_slug': 'web-security', 'question_text': 'What is the fundamental root cause of SQL Injection (SQLi) vulnerabilities in web applications?', 'option_a': 'Using PostgreSQL instead of MongoDB', 'option_b': 'Concatenating untrusted user input directly into dynamic database query strings without parameterized statements or ORMs', 'option_c': 'Hosting websites without SSL certificates', 'option_d': 'Using CSS styles that are outdated', 'correct_answer': 'B', 'explanation': 'SQLi occurs when user inputs are interpreted as SQL commands by the database engine. Using parameterized queries ensures user input is strictly treated as data.'},
    {'topic_slug': 'web-security', 'question_text': 'In Cross-Site Scripting (XSS), what does an attacker inject into a vulnerable web application?', 'option_a': 'A malicious SQL drop database command', 'option_b': 'Malicious client-side scripts (usually JavaScript) that execute in the browser of another unsuspecting user', 'option_c': 'Physical Trojan horse files into server RAM', 'option_d': 'Corrupted image files that crash the monitor', 'correct_answer': 'B', 'explanation': 'XSS allows attackers to execute arbitrary JavaScript in victim browsers, allowing them to steal session cookies, hijack accounts, or redirect to malicious domains.'},
    {'topic_slug': 'web-security', 'question_text': 'What is Cross-Site Request Forgery (CSRF)?', 'option_a': 'Cracking an SSL certificate key', 'option_b': 'An attack that tricks an authenticated user into submitting unwanted state-changing HTTP requests to a trusted application without their knowledge', 'option_c': 'Injecting malicious fonts into HTML pages', 'option_d': 'Flooding an email inbox with spam', 'correct_answer': 'B', 'explanation': 'CSRF abuses the browser\'s automatic transmission of authenticated session cookies to forge actions (e.g. changing passwords or transferring funds) on behalf of the victim.'},
    {'topic_slug': 'web-security', 'question_text': 'What defense mechanism prevents Cross-Site Scripting (XSS) in modern template engines like Jinja2?', 'option_a': 'Compiling Python into C binaries', 'option_b': 'Automated context-aware HTML output escaping, converting characters like < and > into harmless HTML entities (&lt; and &gt;)', 'option_c': 'Encrypting all database passwords with MD5', 'option_d': 'Disabling JavaScript in all client browsers', 'correct_answer': 'B', 'explanation': 'Context-aware auto-escaping ensures user-submitted HTML/JS tags are rendered as plain text entities rather than executed as active scripts by the browser.'},
    {'topic_slug': 'web-security', 'question_text': 'What does the HTTP security header "Strict-Transport-Security" (HSTS) instruct web browsers to do?', 'option_a': 'Strictly block all incoming images', 'option_b': 'Refuse all unencrypted HTTP connections and exclusively communicate with the domain over secure HTTPS', 'option_c': 'Delete cookies when the browser closes', 'option_d': 'Require a 20-character password to access the website', 'correct_answer': 'B', 'explanation': 'HSTS prevents SSL stripping and downgrade attacks by instructing browsers to automatically convert all HTTP links to HTTPS before sending network requests.'}
]

def seed():
    with app.app_context():
        # Create or update admin user
        admin = User.query.filter_by(email='admin@cybersec.com').first()
        if not admin:
            admin = User(username='admin', email='admin@cybersec.com', is_admin=True)
            admin.set_password('Admin@1234')
            db.session.add(admin)
            print('✅ Admin user created: admin@cybersec.com / Admin@1234')
        else:
            print('ℹ️ Admin user already exists.')

        # Create or update topics
        topic_map = {}
        for t in TOPICS:
            existing = Topic.query.filter_by(slug=t['slug']).first()
            if not existing:
                topic = Topic(**t)
                db.session.add(topic)
                db.session.flush()
                topic_map[t['slug']] = topic
                print(f'✅ Created Topic: [{t["level"]}] {t["title"]}')
            else:
                existing.title = t['title']
                existing.description = t['description']
                existing.content = t['content']
                existing.icon = t['icon']
                existing.order = t['order']
                existing.level = t.get('level', 'Basic')
                topic_map[t['slug']] = existing
                print(f'🔄 Updated Topic: [{t.get("level", "Basic")}] {t["title"]}')

        db.session.commit()

        # Create or update questions
        questions_added = 0
        for q in QUESTIONS:
            slug = q.pop('topic_slug')
            topic = topic_map.get(slug)
            if topic:
                existing_q = Question.query.filter_by(question_text=q['question_text']).first()
                if not existing_q:
                    question = Question(topic_id=topic.id, **q)
                    db.session.add(question)
                    questions_added += 1
                else:
                    existing_q.topic_id = topic.id
                    existing_q.option_a = q['option_a']
                    existing_q.option_b = q['option_b']
                    existing_q.option_c = q['option_c']
                    existing_q.option_d = q['option_d']
                    existing_q.correct_answer = q['correct_answer']
                    existing_q.explanation = q['explanation']
            q['topic_slug'] = slug  # restore

        db.session.commit()
        print(f'✅ Added {questions_added} new questions. Total questions in database: {Question.query.count()}')
        print(f'✅ Total topics in database: {Topic.query.count()}')
        print('\n🎉 Database enriched with Basic, Intermediate & Advanced tiers successfully!')

if __name__ == '__main__':
    seed()
