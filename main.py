from manim import *

class IPAddressExplainer(Scene):
    def construct(self):
        # === TITLE ===
        title = Text("Internet Addressing: IPv4, IPv6, and MAC Addresses", font_size=40, color=YELLOW)
        self.play(Write(title))
        self.wait(1.5)
        self.play(title.animate.to_edge(UP))

        # === INTRODUCTION ===
        intro = Text(
            "Every networked device must have a unique identifier to send and receive data.",
            font_size=25
        )
        self.play(FadeIn(intro, shift=UP))
        self.wait(2)
        self.play(FadeOut(intro))

        # === IPv4 SECTION ===
        ipv4_title = Text("IPv4 (Internet Protocol version 4)", font_size=36, color=BLUE)
        ipv4_example = Text("Example: 192.168.0.1", font_size=32)
        ipv4_structure = Text("Structure: 32-bit address → four 8-bit octets", font_size=28, color=GREY_B)
        ipv4_space = Text("Total possible addresses: 2³² ≈ 4.3 billion", font_size=28, color=GREY_B)
        ipv4_group = VGroup(ipv4_title, ipv4_example, ipv4_structure, ipv4_space).arrange(DOWN, buff=0.3)
        self.play(FadeIn(ipv4_group, shift=UP))
        self.wait(3)

        boxes = VGroup(*[Square(side_length=0.6, color=BLUE) for _ in range(4)])
        boxes.arrange(RIGHT, buff=0.2).next_to(ipv4_group, DOWN, buff=0.5)
        labels = VGroup(*[Text(str(i), font_size=20) for i in range(1, 5)])
        for i, lbl in enumerate(labels):
            lbl.next_to(boxes[i], DOWN, buff=0.1)
        self.play(Create(boxes), Write(labels))
        self.wait(1.5)

        exhausted = Text("IPv4 exhaustion due to global device growth", font_size=26, color=RED)
        exhausted.next_to(boxes, DOWN, buff=0.5)
        self.play(Write(exhausted))
        self.wait(2)
        self.play(FadeOut(ipv4_group), FadeOut(boxes), FadeOut(labels), FadeOut(exhausted))

        # === IPv6 SECTION ===
        ipv6_title = Text("IPv6 (Internet Protocol version 6)", font_size=36, color=GREEN)
        ipv6_example = Text("Example: 2001:0db8:85a3::8a2e:0370:7334", font_size=28)
        ipv6_structure = Text("Structure: 128-bit address → eight 16-bit blocks", font_size=28, color=GREY_B)
        ipv6_space = Text("Total possible addresses: 2¹²⁸ ≈ 3.4 × 10³⁸", font_size=28, color=GREY_B)
        ipv6_group = VGroup(ipv6_title, ipv6_example, ipv6_structure, ipv6_space).arrange(DOWN, buff=0.3)
        self.play(FadeIn(ipv6_group, shift=UP))
        self.wait(3)

        hex_boxes = VGroup(*[Square(side_length=0.45, color=GREEN) for _ in range(8)])
        hex_boxes.arrange(RIGHT, buff=0.15).next_to(ipv6_group, DOWN, buff=0.5)
        hex_labels = VGroup(*[Text(hex(i)[2:].upper(), font_size=16) for i in range(8)])
        for i, lbl in enumerate(hex_labels):
            lbl.next_to(hex_boxes[i], DOWN, buff=0.1)
        self.play(Create(hex_boxes), Write(hex_labels))
        self.wait(1.5)

        futureproof = Text("IPv6 ensures scalability for future global connectivity", font_size=26, color=YELLOW)
        futureproof.next_to(hex_boxes, DOWN, buff=0.5)
        self.play(Write(futureproof))
        self.wait(2)
        self.play(FadeOut(ipv6_group), FadeOut(hex_boxes), FadeOut(hex_labels), FadeOut(futureproof))

        # === MAC ADDRESS SECTION ===
        mac_title = Text("MAC (Media Access Control) Address", font_size=36, color=PURPLE)
        mac_example = Text("Example: 00:1A:2B:3C:4D:5E", font_size=30)
        mac_structure = Text("Structure: 48-bit hardware identifier (6 octets)", font_size=28, color=GREY_B)
        mac_purpose = Text("Assigned to the network interface card (NIC)", font_size=28, color=GREY_B)
        mac_group = VGroup(mac_title, mac_example, mac_structure, mac_purpose).arrange(DOWN, buff=0.3)
        self.play(FadeIn(mac_group, shift=UP))
        self.wait(3)

        mac_boxes = VGroup(*[Square(side_length=0.5, color=PURPLE) for _ in range(6)])
        mac_boxes.arrange(RIGHT, buff=0.15).next_to(mac_group, DOWN, buff=0.5)
        mac_labels = VGroup(*[Text(str(i+1), font_size=18) for i in range(6)])
        for i, lbl in enumerate(mac_labels):
            lbl.next_to(mac_boxes[i], DOWN, buff=0.1)
        self.play(Create(mac_boxes), Write(mac_labels))
        self.wait(1.5)
        self.play(FadeOut(mac_group), FadeOut(mac_boxes), FadeOut(mac_labels))

        # === NETWORK CONTEXT (IMPROVED) ===
        net_title = Text("How They Work Together", font_size=30, color=YELLOW)
        self.play(Write(net_title))
        self.wait(0.5)
        self.play(FadeOut(net_title))
        router = Circle(radius=0.5, color=GREY_B).set_fill(BLUE, opacity=0.2)
        router_label = Text("Router", font_size=22).next_to(router, DOWN, buff=0.2)
        router_group = VGroup(router, router_label).shift(DOWN)

        device1 = Square(side_length=0.7, color=BLUE).set_fill(BLUE, opacity=0.1)
        device2 = Square(side_length=0.7, color=GREEN).set_fill(GREEN, opacity=0.1)
        device3 = Square(side_length=0.7, color=PURPLE).set_fill(PURPLE, opacity=0.1)
        devices = VGroup(device1, device2, device3).arrange(RIGHT, buff=2.5).next_to(router, UP, buff=2)

        arrows = VGroup(*[Arrow(router.get_top(), d.get_bottom(), buff=0.1, color=WHITE, stroke_width=3) for d in devices])

        self.play(FadeIn(router_group))
        self.play(FadeIn(devices))
        for arrow in arrows:
            self.play(GrowArrow(arrow), run_time=0.4)

        label_texts = ["IPv4 / IPv6", "IPv6", "MAC Address"]
        label_colors = [BLUE, GREEN, PURPLE]
        labels = VGroup(*[
            Text(text, font_size=22, color=color).next_to(devices[i], UP, buff=0.4)
            for i, (text, color) in enumerate(zip(label_texts, label_colors))
        ])
        self.play(LaggedStart(*[Write(lbl) for lbl in labels], lag_ratio=0.3))
        self.wait(3)

        self.play(
            FadeOut(router_group),
            FadeOut(devices),
            FadeOut(arrows),
            FadeOut(labels)
        )

        # === SUMMARY COMPARISON ===
        summary_title = Text("Summary: Network vs Hardware Identity", font_size=36, color=YELLOW)
        ipv_text = Text("IPv4 / IPv6: Logical (Network-level) identity", font_size=28, color=BLUE)
        mac_text = Text("MAC Address: Physical (Hardware-level) identity", font_size=28, color=PURPLE)
        arrow = Arrow(start=ipv_text.get_bottom(), end=mac_text.get_top(), buff=0.3, color=WHITE)
        summary = VGroup(summary_title, ipv_text, arrow, mac_text).arrange(DOWN, buff=0.4)
        self.play(Write(summary_title))
        self.wait(1)
        self.play(FadeIn(ipv_text), GrowArrow(arrow), FadeIn(mac_text))
        self.wait(3)

        outro = Text("Mohammad K, Davis H, Payden W", font_size=25, color=YELLOW)
        self.play(FadeOut(summary), FadeIn(outro, shift=UP))
        self.wait(1.5)
        self.play(FadeOut(outro))
