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
    {
        'title': 'Password Security & Credential Hygiene',
        'slug': 'password-security',
        'icon': '🔑',
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
        'title': 'Malware, Ransomware & Spyware Defense',
        'slug': 'malware',
        'icon': '🦠',
        'order': 3,
        'description': 'Understand malware variants, zero-day threats, ransomware lifecycles, and defense strategies.',
        'content': '''<h4>1. What is Malware?</h4>
<p>Malware (short for <em>Malicious Software</em>) encompasses any software program specifically designed to compromise confidentiality, integrity, or availability of a host computer or network. In 2023 alone, over <strong>5.4 billion malware attacks</strong> were recorded globally.</p>

<h4>2. Classification of Malicious Software</h4>
<ul>
  <li><strong>Ransomware:</strong> Encrypts the victim's critical files using unbreakable asymmetric ciphers (e.g., RSA-4096 / AES-256) and demands ransom payments in cryptocurrency. Famous examples: <em>WannaCry</em>, <em>Ryuk</em>, <em>LockBit</em>.</li>
  <li><strong>Trojans:</strong> Disguised as legitimate, desirable software (such as game cracks or utility tools) that secretly opens a backdoor (Remote Access Trojan / RAT).</li>
  <li><strong>Spyware & Keyloggers:</strong> Operates silently in the background recording keystrokes, capturing screen activity, and streaming credentials to an external Command and Control (C2) server.</li>
  <li><strong>Rootkits:</strong> Deeply embedded malware that infects the master boot record (MBR) or OS kernel, masking its presence from conventional task managers and basic antivirus software.</li>
  <li><strong>Worms:</strong> Self-replicating standalone software that spreads across computer networks exploiting unpatched vulnerabilities without needing human intervention.</li>
</ul>

<h4>3. The 3-2-1 Backup Strategy (The Ultimate Ransomware Antidote)</h4>
<p>Never negotiate with ransomware criminals. The only guaranteed recovery method is following the <strong>3-2-1 Backup Rule</strong>:</p>
<ul>
  <li>Maintain <strong>3</strong> copies of all critical data (1 primary copy and 2 backups).</li>
  <li>Store backups on <strong>2</strong> different media types (e.g., Internal SSD and External Hard Drive / NAS).</li>
  <li>Keep at least <strong>1</strong> backup copy <strong>Off-site or in an immutable cloud bucket</strong> (disconnected from your local network).</li>
</ul>

<h4>4. Core Defense Recommendations</h4>
<ul>
  <li><strong>Patch Promptly:</strong> Over 60% of breaches exploit vulnerabilities for which a patch was already available. Keep your OS, browsers, and software updated automatically.</li>
  <li><strong>Principle of Least Privilege:</strong> Do not operate your computer daily using a local Administrator account. Standard user accounts prevent malware from modifying system files.</li>
  <li><strong>Active Protection:</strong> Utilize built-in endpoint security (Windows Defender) or reputable suites with behavioral heuristic analysis.</li>
</ul>'''
    },
    {
        'title': 'Social Engineering & Human Hacking',
        'slug': 'social-engineering',
        'icon': '👤',
        'order': 4,
        'description': 'Recognize psychological manipulation, pretexting, baiting, and physical security intrusions.',
        'content': '''<h4>1. Hacking the Human Firewall</h4>
<p>Famed security consultant Kevin Mitnick famously stated: <em>"The human factor is truly the weakest link in security."</em> Social engineering bypasses cryptographic algorithms and firewalls by exploiting fundamental human tendencies: trust, desire to help, fear of authority, and curiosity.</p>

<h4>2. Key Psychological Vectors Exploited</h4>
<ul>
  <li><strong>Authority:</strong> Attackers pretend to be senior executives, police officers, or IT directors to command obedience.</li>
  <li><strong>Urgency:</strong> Fabricating a high-stakes scenario (e.g., "The CEO needs this gift card/wire transfer right now before a client meeting").</li>
  <li><strong>Scarcity & Greed:</strong> Enticing targets with exclusive opportunities, lotteries, or high-return financial investments.</li>
  <li><strong>Sympathy & Social Proof:</strong> Mentioning names of legitimate colleagues to establish instant unverified trust.</li>
</ul>

<h4>3. Common In-Person and Digital Tactics</h4>
<ul>
  <li><strong>Pretexting:</strong> Inventing a comprehensive fictional persona and backstory to extract sensitive details (e.g., calling an employee pretending to conduct a security audit).</li>
  <li><strong>Baiting:</strong> Leaving an infected USB flash drive labeled "Q4 Executive Bonuses" in a company cafeteria or parking lot. Curious employees insert it into office workstations, triggering instant malware execution.</li>
  <li><strong>Tailgating / Piggybacking:</strong> Physically following an authorized employee through a secure keycard-locked door by carrying heavy boxes and asking them to hold the door.</li>
  <li><strong>Quid Pro Quo:</strong> Offering a fake service (such as "free software technical assistance") in return for credentials or remote desktop access.</li>
  <li><strong>Shoulder Surfing:</strong> Visually spying on keyboards, PIN pads, or laptop screens in public places like airports or coffee shops.</li>
</ul>

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
        'title': 'Safe Browsing & Web Security',
        'slug': 'safe-browsing',
        'icon': '🌐',
        'order': 5,
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
    {
        'title': 'Multi-Factor Authentication (MFA / 2FA)',
        'slug': '2fa',
        'icon': '🔐',
        'order': 6,
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
        'order': 7,
        'description': 'Protect your traffic against packet sniffing, Man-in-the-Middle attacks, and rogue hotspots.',
        'content': '''<h4>1. The Inherent Danger of Public Wi-Fi</h4>
<p>Public wireless networks in airports, hotels, cafes, and train stations are designed for maximum convenience, which usually means <strong>zero network-level encryption</strong>. Anyone within radio range equipped with free network monitoring software (such as <em>Wireshark</em>) can monitor unencrypted transmissions broadcast across the radio frequencies.</p>

<h4>2. Prominent Public Wi-Fi Attack Vectors</h4>
<ul>
  <li><strong>Man-in-the-Middle (MitM) Attacks:</strong> An attacker inserts their computer between your laptop and the internet router. All your network requests route through the attacker's machine first, allowing them to inspect, capture, or alter your data.</li>
  <li><strong>Evil Twin Attack:</strong> A cybercriminal configures a rogue Wi-Fi access point with the exact same name (SSID) as the venue (e.g., <em>"Starbucks_Guest_WiFi"</em>). Devices set to auto-connect automatically link to the attacker's hotspot.</li>
  <li><strong>Packet Sniffing:</strong> Intercepting and decoding raw network packets traversing the local wireless local area network (WLAN).</li>
  <li><strong>SSL Stripping:</strong> Attackers downgrade your connection from secure HTTPS to unencrypted HTTP, stripping the encryption layer so login forms submit in plain readable text.</li>
  <li><strong>Malicious Hotspot Injections:</strong> Rogue routers serving fake firmware updates or popups requesting software installation before granting internet access.</li>
</ul>

<h4>3. Best Practices for Traveling and Remote Work</h4>
<ol>
  <li><strong>Always Use a Trusted VPN:</strong> A Virtual Private Network encrypts 100% of your internet traffic inside an encrypted tunnel, rendering sniffed packets completely unintelligible to eavesdroppers.</li>
  <li><strong>Turn Off Auto-Connect:</strong> Disable your smartphone and laptop settings that allow automatic connections to available open Wi-Fi networks.</li>
  <li><strong>Prefer Mobile Data Hotspots:</strong> When dealing with sensitive tasks like banking or exam submissions, tether to your personal smartphone cellular data instead of public Wi-Fi.</li>
  <li><strong>Disable File Sharing:</strong> On Windows, ensure your network profile is set to <strong>"Public Network"</strong> to disable file sharing, network discovery, and local printer access.</li>
  <li><strong>Forget the Network:</strong> Once finished at a public venue, instruct your device to "Forget this Network" so it does not probe for the SSID in other locations.</li>
</ol>'''
    },
    {
        'title': 'Mobile Device Security & App Safety',
        'slug': 'mobile-security',
        'icon': '📱',
        'order': 8,
        'description': 'Defend smartphones against rogue app permissions, spyware, sideloading risks, and physical loss.',
        'content': '''<h4>1. The Smartphone as the Master Key</h4>
<p>Smartphones are no longer just communication devices; they hold your banking apps, private emails, two-factor authentication tokens, personal photos, and biometric profiles. Consequently, mobile operating systems (Android and iOS) have become prime targets for state-sponsored spyware and financial fraudsters.</p>

<h4>2. Major Mobile Threat Vectors</h4>
<ul>
  <li><strong>Malicious Applications (Trojan Droppers):</strong> Apps disguised as calculators, PDF scanners, or games that request excessive permissions to siphon data or send unauthorized premium SMS messages.</li>
  <li><strong>Sideloading Risks:</strong> Downloading `.apk` files from untrusted third-party websites or Telegram channels bypasses the security scrutiny of official app stores.</li>
  <li><strong>Over-Privileged Apps:</strong> Simple apps requesting access to your microphone, camera, contacts, SMS, and background location without legitimate functional necessity.</li>
  <li><strong>Spyware (e.g., Pegasus):</strong> Advanced zero-click exploits that infect mobile devices via missed calls or silent messaging payloads without requiring any user interaction.</li>
  <li><strong>Juice Jacking:</strong> Compromised public USB charging stations at transit hubs that transfer malware or clone data through the USB data pins while you charge your phone.</li>
</ul>

<h4>3. The Golden Rules of Mobile Hygiene</h4>
<ul>
  <li><strong>Official Stores Only:</strong> Restrict app installations strictly to Google Play Store and Apple App Store. Verify developer names, download counts, and recent reviews.</li>
  <li><strong>Audit Permissions Periodically:</strong> Go to <em>Settings → Privacy → Permission Manager</em> and revoke Camera, Location, and Microphone access from apps that do not actively require them.</li>
  <li><strong>Enable Biometrics & Strong Passcodes:</strong> Use at least a 6-digit alphanumeric PIN or biometric unlock (Fingerprint / Face ID). Avoid predictable patterns like "L" shapes or "1234".</li>
  <li><strong>Activate Remote Tracking & Wipe:</strong> Ensure <em>Find My Device</em> (Android) or <em>Find My</em> (Apple) is enabled so you can remotely track, lock, or factory reset your device if stolen.</li>
  <li><strong>Use USB Data Blockers:</strong> When charging in airports, use a "USB condom" (data blocker adapter) that physically disconnects data pins and allows only power transfer.</li>
</ul>'''
    },
]

QUESTIONS = [
    # Topic 1: Password Security (3 Questions)
    {'topic_slug': 'password-security', 'question_text': 'Which of the following password strategies provides the highest mathematical resistance against modern brute-force attacks?', 'option_a': 'An 8-character password with symbols like P@ssw0rd', 'option_b': 'A 20-character multi-word passphrase like correct-horse-battery-staple', 'option_c': 'Using your mother\'s maiden name followed by your birth year', 'option_d': 'Changing a single number in your password every month', 'correct_answer': 'B', 'explanation': 'Passphrases with high character length (16+ characters) have exponentially higher entropy, taking millions of years to crack even on multi-GPU cracking rigs.'},
    {'topic_slug': 'password-security', 'question_text': 'What is a "Credential Stuffing" attack?', 'option_a': 'Guessing passwords using common dictionary words', 'option_b': 'Automating logins on various services using username/password pairs leaked from other data breaches', 'option_c': 'Intercepting passwords over unencrypted HTTP connections', 'option_d': 'Physically looking over someone\'s shoulder while they type', 'correct_answer': 'B', 'explanation': 'Credential stuffing relies on the human tendency to reuse passwords across multiple websites. Attackers test leaked credentials from one breach on hundreds of other platforms.'},
    {'topic_slug': 'password-security', 'question_text': 'What is the primary advantage of using a dedicated Password Manager?', 'option_a': 'It stores passwords on a public website for easy recovery', 'option_b': 'It allows using unique, random, high-complexity passwords for every service while remembering only one master key', 'option_c': 'It automatically disables two-factor authentication to speed up logins', 'option_d': 'It shares your passwords securely with your social media friends', 'correct_answer': 'B', 'explanation': 'Password managers solve the cognitive impossibility of remembering dozens of 20-character random passwords, allowing each service to have a completely unique key.'},

    # Topic 2: Phishing (3 Questions)
    {'topic_slug': 'phishing', 'question_text': 'Which of the following is an example of "Spear Phishing"?', 'option_a': 'Sending 10 million generic fake Netflix renewal emails to random addresses', 'option_b': 'A tailored email to an accounting officer containing their real project name requesting urgent vendor invoice payment', 'option_c': 'Calling a random telephone number pretending to be Windows technical support', 'option_d': 'An automated popup ad claiming your computer has 5 viruses', 'correct_answer': 'B', 'explanation': 'Spear phishing is customized and targeted at a specific individual or organization using researched information to make the fraud appear authentic.'},
    {'topic_slug': 'phishing', 'question_text': 'What is a "Homograph / Punycode" phishing attack?', 'option_a': 'Using a phone call combined with an email', 'option_b': 'Registering lookalike domains using foreign alphabet characters that visually resemble Latin letters', 'option_c': 'Sending an SMS message instead of an email', 'option_d': 'Hacking an official company Twitter account', 'correct_answer': 'B', 'explanation': 'Homograph attacks use internationalized domain names (IDNs) with characters from Cyrillic or Greek that appear identical to Latin characters (e.g. Cyrillic "а" instead of Latin "a").'},
    {'topic_slug': 'phishing', 'question_text': 'What should you do immediately if you realize you entered credentials on a fraudulent phishing website?', 'option_a': 'Wait 24 hours to see if any charges appear on your credit card', 'option_b': 'Disconnect from the internet, change your passwords from another device, and alert your security team', 'option_c': 'Reply to the phishing email demanding they delete your information', 'option_d': 'Restart your computer and continue browsing', 'correct_answer': 'B', 'explanation': 'Fast incident response is vital: disconnect the compromised device, immediately reset passwords from a clean device, enable MFA, and report the compromise.'},

    # Topic 3: Malware (3 Questions)
    {'topic_slug': 'malware', 'question_text': 'What distinguishes a "Computer Worm" from a conventional "Computer Virus"?', 'option_a': 'Worms only infect mobile phones, while viruses only infect desktop PCs', 'option_b': 'A worm can self-replicate and spread autonomously across networks without human intervention or host file attachment', 'option_c': 'Viruses can never be detected by antivirus software', 'option_d': 'Worms only delete files, whereas viruses only display ads', 'correct_answer': 'B', 'explanation': 'Viruses require a host file and human action (e.g. executing an infected program) to propagate. Worms are standalone programs that replicate autonomously over networks.'},
    {'topic_slug': 'malware', 'question_text': 'In the "3-2-1 Backup Strategy", what does the number "1" represent?', 'option_a': 'At least 1 backup must be kept offsite or in an immutable/disconnected cloud location', 'option_b': 'Only 1 person should know the backup password', 'option_c': 'Backups should only be created 1 time per year', 'option_d': 'All data must fit onto 1 USB thumb drive', 'correct_answer': 'A', 'explanation': 'The "1" in 3-2-1 requires at least one backup to be maintained off-site or disconnected from the local network, protecting it against fire, theft, or network-wide ransomware.'},
    {'topic_slug': 'malware', 'question_text': 'What type of malware operates stealthily to record keystrokes and capture sensitive banking credentials?', 'option_a': 'Adware', 'option_b': 'Keylogger / Spyware', 'option_c': 'Defragmenter', 'option_d': 'Ransomware', 'correct_answer': 'B', 'explanation': 'Keyloggers and spyware run silently in the background, logging every keystroke (including passwords and credit card numbers) and exfiltrating them to an adversary.'},

    # Topic 4: Social Engineering (3 Questions)
    {'topic_slug': 'social-engineering', 'question_text': 'What is "Baiting" in the context of physical social engineering?', 'option_a': 'Holding a secure door open for someone who forgot their badge', 'option_b': 'Leaving an infected USB drive in a public area hoping an employee plugs it into a company computer', 'option_c': 'Sending an urgent email pretending to be the company CEO', 'option_d': 'Calling an employee pretending to perform an IT support audit', 'correct_answer': 'B', 'explanation': 'Baiting uses physical media (like an infected USB drive labeled "Confidential Payroll") to exploit human curiosity or greed, enticing victims into running malicious payloads.'},
    {'topic_slug': 'social-engineering', 'question_text': 'What is "Tailgating" (or Piggybacking) in cybersecurity physical security?', 'option_a': 'Following an authorized person through a secured door without scanning a valid credential', 'option_b': 'Installing multiple antivirus scanners on the same computer', 'option_c': 'Copying someone\'s homework in a computer lab', 'option_d': 'Sending repeated phishing emails after the first one is ignored', 'correct_answer': 'A', 'explanation': 'Tailgating occurs when an unauthorized person closely follows an authorized employee into a restricted physical facility, often exploiting polite customs like holding doors.'},
    {'topic_slug': 'social-engineering', 'question_text': 'Why do social engineering attacks rely heavily on creating artificial urgency?', 'option_a': 'Because network firewalls only operate during business hours', 'option_b': 'Because cognitive panic and rushed decisions suppress critical thinking and verification protocols', 'option_c': 'Because phishing emails expire after 10 minutes', 'option_d': 'Because banks shut down servers every evening', 'correct_answer': 'B', 'explanation': 'Urgency induces stress and panic, prompting victims to bypass standard verification procedures and comply before their rational skepticism can evaluate the situation.'},

    # Topic 5: Safe Browsing (3 Questions)
    {'topic_slug': 'safe-browsing', 'question_text': 'Does the padlock icon (HTTPS) mean that a website is guaranteed to be safe and legitimate?', 'option_a': 'Yes, HTTPS certificates are only issued to verified non-profit organizations', 'option_b': 'No, HTTPS only encrypts communication in transit; cybercriminals can easily obtain SSL certificates for phishing sites', 'option_c': 'Yes, HTTPS automatically deletes all malware from your computer', 'option_d': 'No, HTTPS means the website is running without a firewall', 'correct_answer': 'B', 'explanation': 'HTTPS guarantees encryption between your browser and the target server, preventing eavesdropping. However, a phishing site can also use HTTPS encryption.'},
    {'topic_slug': 'safe-browsing', 'question_text': 'What is a "Drive-by Download"?', 'option_a': 'Downloading software while connected to an automobile Wi-Fi hotspot', 'option_b': 'Unintended download and execution of malicious code that occurs automatically simply by visiting a compromised webpage', 'option_c': 'A software update downloaded while the user is away from their keyboard', 'option_d': 'Transferring files between two laptops via Bluetooth', 'correct_answer': 'B', 'explanation': 'Drive-by downloads exploit unpatched browser or plugin vulnerabilities to execute malware automatically without requiring the user to click or accept a download prompt.'},
    {'topic_slug': 'safe-browsing', 'question_text': 'What is the security benefit of utilizing "DNS-over-HTTPS" (DoH)?', 'option_a': 'It increases your internet download speed by 500%', 'option_b': 'It encrypts your domain lookups, preventing local network eavesdroppers and ISPs from tracking the websites you visit', 'option_c': 'It eliminates the need for strong account passwords', 'option_d': 'It automatically cleans browser cookies every 5 seconds', 'correct_answer': 'B', 'explanation': 'Traditional DNS queries are unencrypted plain text. DNS-over-HTTPS (DoH) encrypts these requests, preserving privacy against ISP surveillance and local Wi-Fi eavesdroppers.'},

    # Topic 6: 2FA / MFA (3 Questions)
    {'topic_slug': '2fa', 'question_text': 'Which of the following represents an "Inherence" authentication factor?', 'option_a': 'A 6-digit numeric PIN', 'option_b': 'A hardware YubiKey token', 'option_c': 'A fingerprint or facial recognition scan', 'option_d': 'Your mother\'s maiden name', 'correct_answer': 'C', 'explanation': 'The three factors are: Something you know (Knowledge), Something you have (Possession), and Something you are (Inherence/Biometrics). Biometrics represent inherence.'},
    {'topic_slug': '2fa', 'question_text': 'Why are Hardware Security Keys (FIDO2/WebAuthn) superior to SMS-based 2FA codes?', 'option_a': 'Hardware keys never require an internet connection and are mathematically immune to phishing and SIM swapping', 'option_b': 'Hardware keys automatically guess your password if you forget it', 'option_c': 'SMS codes are limited to only 4 digits', 'option_d': 'Hardware keys can be shared with up to 10 family members simultaneously', 'correct_answer': 'A', 'explanation': 'Hardware keys use cryptographic origin binding that prevents credential harvesting on phishing sites, and they do not rely on cellular networks vulnerable to SIM swapping.'},
    {'topic_slug': '2fa', 'question_text': 'In a "SIM Swap" attack, what action does the cybercriminal take?', 'option_a': 'They steal your physical smartphone from your pocket', 'option_b': 'They deceive your mobile network carrier into transferring your telephone number to a SIM card they control', 'option_c': 'They physically replace your phone battery with a listening device', 'option_d': 'They install a fake SIM card reader on an ATM', 'correct_answer': 'B', 'explanation': 'SIM swapping is social engineering directed at telecom providers to hijack the victim\'s phone number, allowing the attacker to intercept all SMS verification codes.'},

    # Topic 7: Public Wi-Fi (3 Questions)
    {'topic_slug': 'public-wifi', 'question_text': 'What is an "Evil Twin" Wi-Fi attack?', 'option_a': 'A duplicate Wi-Fi password written on a coffee shop chalkboard', 'option_b': 'A rogue wireless access point configured with the same SSID name as a legitimate venue to trick devices into connecting', 'option_c': 'Connecting two smartphones to the same Bluetooth speaker', 'option_d': 'A computer virus that duplicates itself onto two hard drives', 'correct_answer': 'B', 'explanation': 'An Evil Twin is a fraudulent Wi-Fi hotspot set up by an attacker mimicking a legitimate network name (e.g. "Airport_Free_WiFi") to intercept all connected user traffic.'},
    {'topic_slug': 'public-wifi', 'question_text': 'How does a Virtual Private Network (VPN) protect users connected to an untrusted public network?', 'option_a': 'It increases Wi-Fi signal strength through the walls', 'option_b': 'It encapsulates all device traffic inside an encrypted tunnel, rendering intercepted packets unreadable to local eavesdroppers', 'option_c': 'It prevents physical theft of your laptop computer', 'option_d': 'It blocks all incoming emails that contain attachments', 'correct_answer': 'B', 'explanation': 'A VPN creates an encrypted tunnel between your device and the VPN server, ensuring any packet sniffer on the local Wi-Fi network only sees unintelligible encrypted ciphertext.'},
    {'topic_slug': 'public-wifi', 'question_text': 'What is "SSL Stripping"?', 'option_a': 'Removing an SSL certificate from an expired domain', 'option_b': 'A Man-in-the-Middle attack that downgrades secure HTTPS connections to unencrypted HTTP to intercept credentials in plain text', 'option_c': 'Uninstalling antivirus software before running a game', 'option_d': 'Cleaning browser history and cache files', 'correct_answer': 'B', 'explanation': 'In an SSL stripping attack, an adversary intercepts HTTPS requests and serves unencrypted HTTP pages to the victim, capturing submitted passwords and cookies in plain text.'},

    # Topic 8: Mobile Security (3 Questions)
    {'topic_slug': 'mobile-security', 'question_text': 'What is the primary cybersecurity danger of "sideloading" apps from third-party websites rather than official app stores?', 'option_a': 'Sideloaded apps always consume 100% of your device battery within 10 minutes', 'option_b': 'Third-party APK files bypass official malware screening and may contain embedded trojans, spyware, or adware', 'option_c': 'Sideloading requires purchasing a secondary SIM card', 'option_d': 'Sideloaded apps are permanently deleted every time the phone restarts', 'correct_answer': 'B', 'explanation': 'Official app stores screen apps for malicious code and policy violations. Downloading unofficial APKs from forums or websites exposes devices to trojanized payloads.'},
    {'topic_slug': 'mobile-security', 'question_text': 'What is "Juice Jacking"?', 'option_a': 'Drinking energy drinks while coding', 'option_b': 'A cyber attack where compromised public USB charging kiosks install malware or extract data through USB data pins', 'option_c': 'Overclocking a smartphone CPU to increase speed', 'option_d': 'Stealing a smartphone while it is plugged into a wall outlet', 'correct_answer': 'B', 'explanation': 'USB cables transfer both power and data. In a juice jacking attack, compromised charging ports abuse data pins to push malicious code or exfiltrate private files.'},
    {'topic_slug': 'mobile-security', 'question_text': 'Why should smartphone users regularly review and audit app permissions?', 'option_a': 'To ensure apps are using the maximum amount of cellular data possible', 'option_b': 'To prevent over-privileged apps from silently recording audio, accessing locations, or harvesting contacts without a functional need', 'option_c': 'To make sure all apps have access to your bank account details', 'option_d': 'To change the color theme of the mobile operating system', 'correct_answer': 'B', 'explanation': 'Many rogue or monetized apps request permissions far beyond their functional scope (e.g. a flashlight app requesting contacts and microphone access) to harvest and sell user data.'}
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
                print(f'✅ Created Topic: {t["title"]}')
            else:
                existing.title = t['title']
                existing.description = t['description']
                existing.content = t['content']
                existing.icon = t['icon']
                existing.order = t['order']
                topic_map[t['slug']] = existing
                print(f'🔄 Updated Topic: {t["title"]}')

        db.session.commit()

        # Create questions
        questions_added = 0
        for q in QUESTIONS:
            slug = q.pop('topic_slug')
            topic = topic_map.get(slug)
            if topic and not Question.query.filter_by(question_text=q['question_text']).first():
                question = Question(topic_id=topic.id, **q)
                db.session.add(question)
                questions_added += 1
            q['topic_slug'] = slug  # restore

        db.session.commit()
        print(f'✅ Added {questions_added} new questions. Total questions: {Question.query.count()}')
        print('\n🎉 Database enriched and seeded successfully!')

if __name__ == '__main__':
    seed()
