from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Insert SRMIST logo at x=10, y=8, width=25
        self.image('SRMIST.png', 10, 8, 25)
        
        # Adjust position for the header text below the logo
        self.set_xy(40, 20)  # Moves to x=40, y=20 (adjust as needed)
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, "Operating System Week 2 Internal Practical Assessment", 0, 1, 'C')
        
        # Add vertical space and draw a horizontal line below the header
        self.ln(5)
        self.set_line_width(0.5)
        current_y = self.get_y()  # Current vertical position
        self.line(10, current_y, 200, current_y)
        self.ln(5)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, 'C')

# Revised content with updated signature
content = """
Linux Boot Process Overview

1. Power On:
When the computer is switched on, the boot sequence begins.

2. BIOS Initialization:
The Basic Input/Output System (BIOS) performs essential hardware checks and then searches for a bootable device. It typically scans the floppy, CD-ROM, or hard drive. A key (usually F12 or F2, depending on the system) can be pressed during startup to modify the boot sequence. Once the boot loader is found, BIOS loads and executes it.

3. Master Boot Record (MBR):
The MBR, located in the first sector of the bootable disk (e.g., /dev/hda or /dev/sda), is under 512 bytes in size. It comprises three parts:
- The primary boot loader code (first 446 bytes)
- The partition table (next 64 bytes)
- The boot signature (last 2 bytes)
This record contains details necessary to load the bootloader (e.g., GRUB), transferring control to it.

4. GRUB (Grand Unified Bootloader):
GRUB offers a user-friendly menu to choose from multiple installed kernel images. It displays a splash screen and waits briefly before booting the default kernel if no selection is made. GRUB understands the file system, unlike older loaders like LILO. Its configuration file (typically located at /boot/grub/grub.conf or /etc/grub.conf) specifies the kernel and initial RAM disk (initrd) images to be loaded.

5. Kernel Loading:
After GRUB loads the kernel and initrd into memory, the kernel mounts the root file system (as defined in the bootloader configuration). It then executes the /sbin/init program, which is assigned process ID 1. The initrd (Initial RAM Disk) serves as a temporary root file system, providing necessary drivers until the real root file system is mounted.

6. Init Process and Runlevels:
The init process reads the /etc/inittab file to determine the system's default runlevel. Common runlevels include:
- 0: Halt
- 1: Single-user mode
- 2: Multiuser mode without networking (NFS)
- 3: Full multiuser mode
- 4: Unused
- 5: Graphical mode (X11)
- 6: Reboot

Based on the determined runlevel, init launches corresponding startup programs from directories like /etc/rc.d/rc3.d/ (for runlevel 3) or /etc/rc.d/rc5.d/ (for runlevel 5). In these directories, files starting with S initiate services, and those beginning with K signal processes to be terminated during shutdown. The numbering following S or K indicates the order in which these services are started or stopped.

7. Login Process:
After all runlevel scripts have executed, the system presents a login prompt. Users then:
- Enter their username and password
- Are authenticated by the operating system
- Have a shell spawned based on the information in /etc/passwd
- Are directed to their home directory
- Have their session initialized by system-wide (e.g., /etc/profile) and personal login scripts (e.g., .profile)

Rajesh Nambi
B.A | MCA
rn6525@srmist.edu.in
"""

# Replace problematic Unicode characters if any
content = content.replace("\u2019", "'")

pdf = PDF()
pdf.add_page()

pdf.set_font("Arial", size=12)
for line in content.split('\n'):
    pdf.multi_cell(0, 10, line)

pdf_file = "Week2-OS-IPA.pdf"
pdf.output(pdf_file)
print(f"PDF generated and saved as {pdf_file}")
