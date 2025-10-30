# COMP702/703 Research and Development

## Linux Networking Performance Evaluation (Physical Team)

### Summary

This R&D Project portfolio contains a comprehensive collection of documentation, testing files, configurations, and project management artifacts organised into four main categories:

1. **Research and Upskilling** - Skills matrices, training materials, and virtualisation scripts
2. **Planning and Control** - Project proposals, planning documents, and mid-term review materials
3. **Communication and Teamwork** - Meeting records, logbooks, client communications, and team evidence
4. **Development and Quality Assurance** - Testing methodologies, configuration files, evaluation logs, data analysis tools, and quality assurance checklists

The structure reflects a well-organised academic project with proper version control, comprehensive documentation, and systematic approach to both technical implementation and project management.

---

### File Completeness Analysis

#### Evaluation Testing Log Files Status

| Distribution | IPv4 TCP | IPv4 UDP | IPv6 TCP | IPv6 UDP | Total | Status       |
| ------------ | -------- | -------- | -------- | -------- | ----- | ------------ |
| **Ubuntu**   | 12/12 ✅ | 12/12 ✅ | 12/12 ✅ | 12/12 ✅ | 48/48 | Complete     |
| **Fedora**   | 12/12 ✅ | 12/12 ✅ | 12/12 ✅ | 12/12 ✅ | 48/48 | Complete     |
| **Kali**     | 12/12 ✅ | 12/12 ✅ | 12/12 ✅ | 12/12 ✅ | 48/48 | **Complete** |

#### Outcome

✅ **All evaluation testing log files are now complete!**

All three Linux distributions (Ubuntu, Fedora, and Kali) now have complete sets of:

- IPv4 TCP testing logs (12 files each)
- IPv4 UDP testing logs (12 files each)
- IPv6 TCP testing logs (12 files each)
- IPv6 UDP testing logs (12 files each)

This ensures comprehensive cross-distribution performance comparisons can be conducted with complete data sets across all testing scenarios.

**Total File Count:** 880 files across all directories and subdirectories.

---

### Project Folder Structure

This document outlines the directory structure for the R&D Project.  
Each section represents a major area of the project, with subfolders for specific resources and outputs.

#### Root Directory

```
Portfolio/
├── .gitignore
├── README.md
└── Team-Portfolio-Submission.pdf
```

#### 01-Research-and-Upskilling/

```
01-Research-and-Upskilling/
├── 01. Skills Matrix.xlsx
└── Upskilling
    ├── 02. Upskilling Management Plan.docx
    ├── D-ITG-2.8.1-manual.pdf
    ├── QEMU
    │   ├── macOS
    │   │   ├── fedora.sh
    │   │   ├── kali.sh
    │   │   └── ubuntu.sh
    │   └── Windows-Linux
    │       ├── fedora.sh
    │       ├── kali.sh
    │       └── ubuntu.sh
    └── Ubuntu CLI Cheat Sheet 2025.pdf
```

#### 02-Planning-and-Control/

```
02-Planning-and-Control/
├── Handover Plan.docx
├── Mid-Term Review
│   ├── Linux Network Evaluation (Physical) Mid-Term Status Report.pdf
│   ├── Status Report.pptx
│   ├── Status Report v1.5.docx
│   └── Version-History
│       ├── Status Report v1.0.docx
│       ├── Status Report v1.1.docx
│       ├── Status Report v1.3.docx
│       └── Status Report v1.4.docx
├── Project Brief.docx
├── Proposal
│   ├── Planning-Documents
│   │   ├── Current
│   │   │   ├── 08. Work Breakdown Structure Diagram v3.png
│   │   │   ├── 08. Work Breakdown Structure v3.1.docx
│   │   │   ├── 09. Gantt Chart v3.mpp
│   │   │   ├── 15. Risk Register v3.xlsx
│   │   │   ├── 16. Issue Log v3.1.docx
│   │   │   ├── 21. Quality Assurance Plan v4.docx
│   │   │   └── Network Diagram.png
│   │   └── Version-History
│   │       ├── v1.0-Initial-Proposal
│   │       │   ├── 01. Scope Statement v1.docx
│   │       │   ├── 02. Stakeholder Register.docx
│   │       │   ├── 03. Communication Management Plan.docx
│   │       │   ├── 04. Stakeholder Management Plan.docx
│   │       │   ├── 05. Network Diagram v1.png
│   │       │   ├── 07. Milestone Report v1.docx
│   │       │   ├── 08. Work Breakdown Structure Diagram v1.png
│   │       │   ├── 08. Work Breakdown Structure v1.docx
│   │       │   ├── 09. Gantt Chart.mpp
│   │       │   ├── 10. Project Charter.docx
│   │       │   ├── 11. Requirement Traceability Matrix v1.xlsx
│   │       │   ├── 12. Team Contract.docx
│   │       │   ├── 13. Client Contract.docx
│   │       │   ├── 14. Team Schedule Table v1.xlsx
│   │       │   ├── 15. Risk Register v1.xlsx
│   │       │   ├── 16. Issue Log v1.docx
│   │       │   ├── 17. Change Management Plan.docx
│   │       │   ├── 21. Quality Assurance Diagram.png
│   │       │   ├── 21. Quality Assurance Plan v1.docx
│   │       │   └── Gantt-Chart-v1
│   │       │       ├── 20. Gantt Chart v1.0.mpp
│   │       │       ├── 20. Gantt Chart v1.1.mpp
│   │       │       ├── 20. Gantt Chart v1.2.mpp
│   │       │       └── 20. Gantt Chart v1.3.mpp
│   │       ├── v2.0-Post-Feedback
│   │       │   ├── 01. Scope Statement v2.docx
│   │       │   ├── 07. Milestone Report Version 2.docx
│   │       │   ├── 08. Work Breakdown Structure Diagram v2.png
│   │       │   ├── 08. Work Breakdown Structure v2.docx
│   │       │   ├── 09. Gantt Chart v2.mpp
│   │       │   ├── 11. Requirement Traceability Matrix v2.xlsx
│   │       │   ├── 14. Team Schedule Table v2.xlsx
│   │       │   ├── 15. Risk Register v2.xlsx
│   │       │   ├── 16. Issue Log v2.docx
│   │       │   ├── 21. Quality Assurance Plan v2.docx
│   │       │   ├── 22. Conflict Resolution Plan.docx
│   │       │   └── Network Diagram.ai
│   │       └── v3.0-Refinements
│   │           ├── 08. Work Breakdown Structure v3.0.docx
│   │           ├── 16. Issue Log v3.docx
│   │           └── 21. Quality Assurance Plan v3.docx
│   ├── Proposal-Document
│   │   ├── Proposal_v2.5.docx
│   │   ├── Proposal_v2.4.pdf
│   │   └── Version-History
│   │       ├── Proposal_v0.1.docx
│   │       ├── Proposal_v1.01.docx
│   │       ├── Proposal_v1.02.docx
│   │       ├── Proposal_v1.03.docx
│   │       ├── Proposal_v1.04.docx
│   │       ├── Proposal_v1.05.docx
│   │       ├── Proposal_v1.0.docx
│   │       ├── Proposal_v1.1.docx
│   │       ├── Proposal_v1.2.docx
│   │       ├── Proposal_v1.3.docx
│   │       ├── Proposal_v1.4.docx
│   │       ├── Proposal_v1.5.docx
│   │       ├── Proposal_v1.6.docx
│   │       ├── Proposal_v1.7.docx
│   │       ├── Proposal_v1.8.docx
│   │       ├── Proposal_v1.9.docx
│   │       ├── Proposal_v2.0.docx
│   │       ├── Proposal_v2.1.docx
│   │       ├── Proposal_v2.2.docx
│   │       ├── Proposal_v2.2_Submission.pdf
│   │       ├── Proposal_v2.3.docx
│   │       └── Proposal_v2.3.pdf
│   └── Proposal-Presentation
│       ├── Proposal Powerpoint.pptx
│       └── Version-History
│           └── First Draft Powerpoint.pptx
└── Status Report v1.6.docx
```

#### 03-Communication-and-Teamwork/

```
03-Communication-and-Teamwork/
├── Attendance.xlsx
├── Client Contract.docx
├── Client Feedback Form.docx
├── Client Feedback Form_signed.pdf
├── Deliverable Acceptance Form.docx
├── Group Details.xlsx
├── Logbooks
│   ├── Evidence
│   │   ├── Larissa
│   │   │   └── Jitter MATLAB Code
│   │   ├── Nathan
│   │   │   ├── dat-converter.py
│   │   │   └── git_commits.txt
│   │   ├── Thomas
│   │   │   ├── D-ITG.pdf
│   │   │   ├── download_ubuntu_packages.sh
│   │   │   ├── export_logs.sh
│   │   │   ├── gpu-driver-fix.png
│   │   │   ├── ip_addresses.txt
│   │   │   ├── ipv4_old.sh
│   │   │   ├── ipv4.sh
│   │   │   ├── ipv4_tcp.sh
│   │   │   ├── ipv6_old.sh
│   │   │   ├── ipv6.sh
│   │   │   ├── linux-1.png
│   │   │   ├── linux-2.png
│   │   │   ├── logins.png
│   │   │   ├── methodology.txt
│   │   │   ├── Network IPs.pdf
│   │   │   └── packetsizes.txt
│   │   └── Win
│   │       └── create_script.sh
│   ├── Logbook - Charmi Patel v2.pdf
│   ├── Logbook - Kylie Afable v2.pdf
│   ├── Logbook - Nathan Quai Hoi v2.pdf
│   ├── Logbook - Thomas Robinson v2.pdf
│   └── Version-History
│       ├── Logbook - Charmi Patel v1.pdf
│       ├── Logbook - Kylie Afable v1.pdf
│       ├── Logbook - Nathan Quai Hoi v1.pdf
│       ├── Logbook - Thomas Robinson v1.pdf
│       ├── Logbook - Win Phyo v1.pdf
│       └── Logbook - Zafar Azad v1.pdf
├── Meetings
│   ├── Agendas
│   │   ├── Project_Status_Meeting_AgendaV2.doc
│   │   ├── Team-Client Kick-off Meeting Agenda.docx
│   │   ├── Team-Client Kick-off Meeting Agenda.pdf
│   │   ├── Team-Client Meeting Agenda 01-05-25.docx
│   │   ├── Team-Client Meeting Agenda 01-05-25.pdf
│   │   ├── Team-Client Meeting Agenda 22-05-25.docx
│   │   ├── Team-Client Meeting Agenda 22-05-25.pdf
│   │   ├── Team-Client Meeting Agenda 27-03-25.docx
│   │   └── Team-Client Meeting Agenda 27-03-25.pdf
│   └── Minutes
│       ├── Mentor-Client-Meetings
│       │   ├── Meeting Minutes 2025-03-20 (Client Kick-off).docx
│       │   ├── Meeting Minutes 2025-03-27 (Mentor).docx
│       │   ├── Meeting Minutes 2025-04-03 (Client).docx
│       │   ├── Meeting Minutes 2025-05-01 (Client).docx
│       │   ├── Meeting Minutes 2025-05-22 (Client).docx
│       │   ├── Meeting Minutes 2025-05-29 (Mentor).docx
│       │   ├── Meeting Minutes 2025-06-05 (Client).docx
│       │   ├── Meeting Minutes 2025-06-18 (Client).docx
│       │   ├── Meeting Minutes 2025-07-31 (Client).docx
│       │   ├── Meeting Minutes 2025-08-14 (Client).docx
│       │   ├── Meeting Minutes 2025-09-04 (Client).docx
│       │   ├── Meeting Minutes 2025-10-02 (Client).docx
│       │   └── Meeting Minutes 2025-10-16 (Client).docx
│       └── Team-Meetings
│           ├── Meeting Minutes 2025-03-18 (Team Kick-off).docx
│           ├── Meeting Minutes 2025-03-20 (Team).docx
│           ├── Meeting Minutes 2025-03-31 (Team).docx
│           ├── Meeting Minutes 2025-04-03 (Team).docx
│           ├── Meeting Minutes 2025-04-04 (Team).docx
│           ├── Meeting Minutes 2025-04-07 (Team).docx
│           ├── Meeting Minutes 2025-04-15 (Team).docx
│           ├── Meeting Minutes 2025-04-22 (Team).docx
│           ├── Meeting Minutes 2025-04-30 (Team).docx
│           ├── Meeting Minutes 2025-05-08 (Team).docx
│           ├── Meeting Minutes 2025-05-15 (Team).docx
│           ├── Meeting Minutes 2025-05-28 (Team).docx
│           ├── Meeting Minutes 2025-06-18 (Team).docx
│           ├── Meeting Minutes 2025-08-14 (Team).docx
│           ├── Meeting Minutes 2025-08-28 (Team).docx
│           ├── Meeting Minutes 2025-09-17 (Team).docx
│           ├── Meeting Minutes 2025-09-25 (Team).docx
│           ├── Meeting Minutes 2025-10-15 (Team).docx
│           ├── Meeting Minutes 2025-10-16 (Team).docx
│           ├── Meeting Minutes 2025-10-27 (Team).docx
│           └── Meeting Minutes 2025-10-28 (Team).docx
└── Timetables.xlsx
```

#### 04-Development-and-Quality-Assurance/

```
04-Development-and-Quality-Assurance/
├── Evaluation-Testing
│   ├── Chrony NTP server time synchronisation.docx
│   ├── Configs
│   │   ├── config_files.sh
│   │   ├── Fedora
│   │   │   ├── pc1
│   │   │   │   ├── etc
│   │   │   │   │   ├── chrony.conf
│   │   │   │   │   ├── netplan
│   │   │   │   │   │   └── 99-netplan.yaml
│   │   │   │   │   └── udev
│   │   │   │   │       └── rules.d
│   │   │   │   │           └── 70-persistent-usb-tether.rules
│   │   │   │   └── home
│   │   │   │       └── sender
│   │   │   │           ├── config_files.sh
│   │   │   │           ├── ipv4.sh
│   │   │   │           └── ipv6.sh
│   │   │   ├── pc2
│   │   │   │   ├── etc
│   │   │   │   │   ├── chrony.conf
│   │   │   │   │   ├── netplan
│   │   │   │   │   │   └── 99-netplan.yaml
│   │   │   │   │   └── udev
│   │   │   │   │       └── rules.d
│   │   │   │   │           └── 70-persistent-usb-tether.rules
│   │   │   │   └── home
│   │   │   │       └── receiver
│   │   │   │           └── export_logs.sh
│   │   │   ├── router1
│   │   │   │   └── etc
│   │   │   │       ├── chrony.conf
│   │   │   │       ├── netplan
│   │   │   │       │   └── 99-netplan.yaml
│   │   │   │       └── udev
│   │   │   │           └── rules.d
│   │   │   │               └── 70-persistent-usb-tether.rules
│   │   │   └── router2
│   │   │       └── etc
│   │   │           ├── chrony.conf
│   │   │           ├── netplan
│   │   │           │   └── 99-netplan.yaml
│   │   │           └── udev
│   │   │               └── rules.d
│   │   │                   └── 70-persistent-usb-tether.rules
│   │   ├── Kali
│   │   │   ├── pc1
│   │   │   │   ├── etc
│   │   │   │   │   ├── chrony
│   │   │   │   │   │   └── chrony.conf
│   │   │   │   │   ├── netplan
│   │   │   │   │   │   └── 99-netplan.yaml
│   │   │   │   │   └── udev
│   │   │   │   │       └── rules.d
│   │   │   │   │           └── 70-persistent-usb-tether.rules
│   │   │   │   └── home
│   │   │   │       └── sender
│   │   │   │           ├── config_files.sh
│   │   │   │           ├── ipv4.sh
│   │   │   │           └── ipv6.sh
│   │   │   ├── pc2
│   │   │   │   ├── etc
│   │   │   │   │   ├── chrony
│   │   │   │   │   │   └── chrony.conf
│   │   │   │   │   ├── netplan
│   │   │   │   │   │   └── 99-netplan.yaml
│   │   │   │   │   └── udev
│   │   │   │   │       └── rules.d
│   │   │   │   │           └── 70-persistent-usb-tether.rules
│   │   │   │   └── home
│   │   │   │       └── receiver
│   │   │   │           └── export_logs.sh
│   │   │   ├── router1
│   │   │   │   └── etc
│   │   │   │       ├── chrony
│   │   │   │       │   └── chrony.conf
│   │   │   │       ├── netplan
│   │   │   │       │   └── 99-netplan.yaml
│   │   │   │       └── udev
│   │   │   │           └── rules.d
│   │   │   │               └── 70-persistent-usb-tether.rules
│   │   │   └── router2
│   │   │       └── etc
│   │   │           ├── chrony
│   │   │           │   └── chrony.conf
│   │   │           ├── netplan
│   │   │           │   └── 99-netplan.yaml
│   │   │           └── udev
│   │   │               └── rules.d
│   │   │                   └── 70-persistent-usb-tether.rules
│   │   └── Ubuntu
│   │       ├── pc1
│   │       │   ├── etc
│   │       │   │   ├── chrony
│   │       │   │   │   └── chrony.conf
│   │       │   │   ├── netplan
│   │       │   │   │   └── 50-cloud-init.yaml
│   │       │   │   └── udev
│   │       │   │       └── rules.d
│   │       │   │           └── 70-persistent-usb-tether.rules
│   │       │   └── home
│   │       │       └── sender
│   │       │           ├── config_files.sh
│   │       │           ├── ipv4.sh
│   │       │           └── ipv6.sh
│   │       ├── pc2
│   │       │   ├── etc
│   │       │   │   ├── chrony
│   │       │   │   │   └── chrony.conf
│   │       │   │   ├── netplan
│   │       │   │   │   └── 50-cloud-init.yaml
│   │       │   │   └── udev
│   │       │   │       └── rules.d
│   │       │   │           └── 70-persistent-usb-tether.rules
│   │       │   └── home
│   │       │       └── receiver
│   │       │           └── export_logs.sh
│   │       ├── router1
│   │       │   └── etc
│   │       │       ├── chrony
│   │       │       │   └── chrony.conf
│   │       │       ├── netplan
│   │       │       │   └── 50-cloud-init.yaml
│   │       │       └── udev
│   │       │           └── rules.d
│   │       │               └── 70-persistent-usb-tether.rules
│   │       └── router2
│   │           └── etc
│   │               ├── chrony
│   │               │   └── chrony.conf
│   │               ├── netplan
│   │               │   └── 50-cloud-init.yaml
│   │               └── udev
│   │                   └── rules.d
│   │                       └── 70-persistent-usb-tether.rules
│   ├── How to run evaluation testing.docx
│   ├── Logs
│   │   ├── clean_data.py
│   │   ├── Compare Data.xlsx
│   │   ├── excel.py
│   │   ├── export_logs.sh
│   │   ├── Fedora
│   │   │   ├── Fedora_Data.xlsx
│   │   │   ├── ipv4_tcp_1024.txt
│   │   │   ├── ipv4_tcp_1152.txt
│   │   │   ├── ipv4_tcp_1280.txt
│   │   │   ├── ipv4_tcp_128.txt
│   │   │   ├── ipv4_tcp_1408.txt
│   │   │   ├── ipv4_tcp_1536.txt
│   │   │   ├── ipv4_tcp_256.txt
│   │   │   ├── ipv4_tcp_384.txt
│   │   │   ├── ipv4_tcp_512.txt
│   │   │   ├── ipv4_tcp_640.txt
│   │   │   ├── ipv4_tcp_768.txt
│   │   │   ├── ipv4_tcp_896.txt
│   │   │   ├── ipv4_udp_1024.txt
│   │   │   ├── ipv4_udp_1152.txt
│   │   │   ├── ipv4_udp_1280.txt
│   │   │   ├── ipv4_udp_128.txt
│   │   │   ├── ipv4_udp_1408.txt
│   │   │   ├── ipv4_udp_1536.txt
│   │   │   ├── ipv4_udp_256.txt
│   │   │   ├── ipv4_udp_384.txt
│   │   │   ├── ipv4_udp_512.txt
│   │   │   ├── ipv4_udp_640.txt
│   │   │   ├── ipv4_udp_768.txt
│   │   │   ├── ipv4_udp_896.txt
│   │   │   ├── ipv6_tcp_1024.txt
│   │   │   ├── ipv6_tcp_1152.txt
│   │   │   ├── ipv6_tcp_1280.txt
│   │   │   ├── ipv6_tcp_128.txt
│   │   │   ├── ipv6_tcp_1408.txt
│   │   │   ├── ipv6_tcp_1536.txt
│   │   │   ├── ipv6_tcp_256.txt
│   │   │   ├── ipv6_tcp_384.txt
│   │   │   ├── ipv6_tcp_512.txt
│   │   │   ├── ipv6_tcp_640.txt
│   │   │   ├── ipv6_tcp_768.txt
│   │   │   ├── ipv6_tcp_896.txt
│   │   │   ├── ipv6_udp_1024.txt
│   │   │   ├── ipv6_udp_1152.txt
│   │   │   ├── ipv6_udp_1280.txt
│   │   │   ├── ipv6_udp_128.txt
│   │   │   ├── ipv6_udp_1408.txt
│   │   │   ├── ipv6_udp_1536.txt
│   │   │   ├── ipv6_udp_256.txt
│   │   │   ├── ipv6_udp_384.txt
│   │   │   ├── ipv6_udp_512.txt
│   │   │   ├── ipv6_udp_640.txt
│   │   │   ├── ipv6_udp_768.txt
│   │   │   └── ipv6_udp_896.txt
│   │   ├── Kali
│   │   │   ├── ipv4_tcp_1024.txt
│   │   │   ├── ipv4_tcp_1152.txt
│   │   │   ├── ipv4_tcp_1280.txt
│   │   │   ├── ipv4_tcp_128.txt
│   │   │   ├── ipv4_tcp_1408.txt
│   │   │   ├── ipv4_tcp_1536.txt
│   │   │   ├── ipv4_tcp_256.txt
│   │   │   ├── ipv4_tcp_384.txt
│   │   │   ├── ipv4_tcp_512.txt
│   │   │   ├── ipv4_tcp_640.txt
│   │   │   ├── ipv4_tcp_768.txt
│   │   │   ├── ipv4_tcp_896.txt
│   │   │   ├── ipv4_udp_1024.txt
│   │   │   ├── ipv4_udp_1152.txt
│   │   │   ├── ipv4_udp_1280.txt
│   │   │   ├── ipv4_udp_128.txt
│   │   │   ├── ipv4_udp_1408.txt
│   │   │   ├── ipv4_udp_1536.txt
│   │   │   ├── ipv4_udp_256.txt
│   │   │   ├── ipv4_udp_384.txt
│   │   │   ├── ipv4_udp_512.txt
│   │   │   ├── ipv4_udp_640.txt
│   │   │   ├── ipv4_udp_768.txt
│   │   │   ├── ipv4_udp_896.txt
│   │   │   ├── ipv6_tcp_1024.txt
│   │   │   ├── ipv6_tcp_1152.txt
│   │   │   ├── ipv6_tcp_1280.txt
│   │   │   ├── ipv6_tcp_128.txt
│   │   │   ├── ipv6_tcp_1408.txt
│   │   │   ├── ipv6_tcp_1536.txt
│   │   │   ├── ipv6_tcp_256.txt
│   │   │   ├── ipv6_tcp_384.txt
│   │   │   ├── ipv6_tcp_512.txt
│   │   │   ├── ipv6_tcp_640.txt
│   │   │   ├── ipv6_tcp_768.txt
│   │   │   ├── ipv6_tcp_896.txt
│   │   │   ├── ipv6_udp_1024.txt
│   │   │   ├── ipv6_udp_1152.txt
│   │   │   ├── ipv6_udp_1280.txt
│   │   │   ├── ipv6_udp_128.txt
│   │   │   ├── ipv6_udp_1408.txt
│   │   │   ├── ipv6_udp_1536.txt
│   │   │   ├── ipv6_udp_256.txt
│   │   │   ├── ipv6_udp_384.txt
│   │   │   ├── ipv6_udp_512.txt
│   │   │   ├── ipv6_udp_640.txt
│   │   │   ├── ipv6_udp_768.txt
│   │   │   ├── ipv6_udp_896.txt
│   │   │   └── Kali_Data.xlsx
│   │   ├── Python-Graphs
│   │   │   ├── Comparison_IPv4_vs_IPv6_Delay.png
│   │   │   ├── Comparison_IPv4_vs_IPv6_Jitter.png
│   │   │   ├── Comparison_IPv4_vs_IPv6_Packet Loss.png
│   │   │   ├── Comparison_IPv4_vs_IPv6_Throughput.png
│   │   │   ├── graphing_compare_ipv4_ipv6.py
│   │   │   ├── graphing_ipv4.py
│   │   │   ├── graphing_ipv6.py
│   │   │   ├── IPv4_Comparison_Delay.png
│   │   │   ├── IPv4_Comparison_Jitter.png
│   │   │   ├── IPv4_Comparison_Packet Loss.png
│   │   │   ├── IPv4_Comparison_Throughput.png
│   │   │   ├── IPv6_Comparison_Delay.png
│   │   │   ├── IPv6_Comparison_Jitter.png
│   │   │   ├── IPv6_Comparison_Packet Loss.png
│   │   │   └── IPv6_Comparison_Throughput.png
│   │   ├── rename.sh
│   │   ├── Ubuntu
│   │   │   ├── ipv4_tcp_1024.txt
│   │   │   ├── ipv4_tcp_1152.txt
│   │   │   ├── ipv4_tcp_1280.txt
│   │   │   ├── ipv4_tcp_128.txt
│   │   │   ├── ipv4_tcp_1408.txt
│   │   │   ├── ipv4_tcp_1536.txt
│   │   │   ├── ipv4_tcp_256.txt
│   │   │   ├── ipv4_tcp_384.txt
│   │   │   ├── ipv4_tcp_512.txt
│   │   │   ├── ipv4_tcp_640.txt
│   │   │   ├── ipv4_tcp_768.txt
│   │   │   ├── ipv4_tcp_896.txt
│   │   │   ├── ipv4_udp_1024.txt
│   │   │   ├── ipv4_udp_1152.txt
│   │   │   ├── ipv4_udp_1280.txt
│   │   │   ├── ipv4_udp_128.txt
│   │   │   ├── ipv4_udp_1408.txt
│   │   │   ├── ipv4_udp_1536.txt
│   │   │   ├── ipv4_udp_256.txt
│   │   │   ├── ipv4_udp_384.txt
│   │   │   ├── ipv4_udp_512.txt
│   │   │   ├── ipv4_udp_640.txt
│   │   │   ├── ipv4_udp_768.txt
│   │   │   ├── ipv4_udp_896.txt
│   │   │   ├── ipv6_tcp_1024.txt
│   │   │   ├── ipv6_tcp_1152.txt
│   │   │   ├── ipv6_tcp_1280.txt
│   │   │   ├── ipv6_tcp_128.txt
│   │   │   ├── ipv6_tcp_1408.txt
│   │   │   ├── ipv6_tcp_1536.txt
│   │   │   ├── ipv6_tcp_256.txt
│   │   │   ├── ipv6_tcp_384.txt
│   │   │   ├── ipv6_tcp_512.txt
│   │   │   ├── ipv6_tcp_640.txt
│   │   │   ├── ipv6_tcp_768.txt
│   │   │   ├── ipv6_tcp_896.txt
│   │   │   ├── ipv6_udp_1024.txt
│   │   │   ├── ipv6_udp_1152.txt
│   │   │   ├── ipv6_udp_1280.txt
│   │   │   ├── ipv6_udp_128.txt
│   │   │   ├── ipv6_udp_1408.txt
│   │   │   ├── ipv6_udp_1536.txt
│   │   │   ├── ipv6_udp_256.txt
│   │   │   ├── ipv6_udp_384.txt
│   │   │   ├── ipv6_udp_512.txt
│   │   │   ├── ipv6_udp_640.txt
│   │   │   ├── ipv6_udp_768.txt
│   │   │   ├── ipv6_udp_896.txt
│   │   │   └── Ubuntu_Data.xlsx
│   │   └── Ubuntu_Fedora_Sample_Graphing.xlsx
│   ├── Methodology - Fedora Server.docx
│   ├── Methodology - Kali Linux.docx
│   ├── Methodology - Ubuntu Server.docx
│   └── Packages
│       ├── Fedora
│       │   └── download_fedora_packages.sh
│       ├── Kali
│       │   └── download_kali_packages.sh
│       └── Ubuntu
│           └── download_ubuntu_packages.sh
├── Poster
│   ├── AUT-logo-black.jpg
│   ├── poster_v3.png
│   ├── qr_code.svg
│   ├── Sections
│   │   ├── 01 Background.docx
│   │   ├── 02 Rationale.docx
│   │   ├── 03 Objectives.docx
│   │   ├── 04 Project Impact.docx
│   │   ├── 05 Goals.docx
│   │   ├── 06 Project Management Methodology.docx
│   │   ├── 07 Artefacts.docx
│   │   ├── 08 Quality Assurance.docx
│   │   ├── 09 Key Challenges.docx
│   │   ├── 10 Lessons Learnt.docx
│   │   ├── 11 References.docx
│   │   └── 12 Acknowledgements.docx
│   └── Version-History
│       ├── poster_v1.png
│       └── poster_v2.png
└── Quality-Assurance
    ├── Completed Checklists
    │   ├── Completed Fedora Checklists.pdf
    │   ├── Completed Kali Checklists.pdf
    │   └── Completed Ubuntu Checklists.pdf
    ├── Peer Review
    │   ├── Peer Review Checklist - Fedora Configuration v1.0.pdf
    │   ├── Peer Review Checklist - Kali Configuration v1.0.pdf
    │   ├── Peer Review Checklist - Ubuntu Configuration v1.1.pdf
    │   └── Version-History
    │       └── Peer Review Checklist - Ubuntu Configuration v1.0.pdf
    ├── QA Metric Report.docx
    ├── QA Phase Entry-Exit Log.docx
    └── Router Configuration
        ├── Router Configuration Checklist - Fedora v1.0.pdf
        ├── Router Configuration Checklist - Kali v1.0.pdf
        ├── Router Configuration Checklist - Ubuntu v1.1.pdf
        └── Version-History
            └── Router Configuration Checklist - Ubuntu v1.0.pdf
```

---

_Last Updated: October 30, 2025_
