"""FreshlyMadeFL shop style. Every product gets one palette; all graphics use these roles.
Fonts: Poppins ExtraBold for headlines (tight letter spacing), Inter for body.
Look: soft pastel background, dark ink headline + bright 'pop' second line, butter-yellow pill,
white cards with ink border, four-point sparkles, soft white blobs in corners.
Thumbnail: 4:3 canvas (2700x2024), all content inside the center square Etsy crops to."""
THEMES = {
    # name: bg, ink (headline/table headers), pop (accent line/kicker), pill, tint (light fills),
    #       line (borders), done (completed rows), text (body)
    "blush": dict(bg="#FCD9E1", ink="#5B1E3C", pop="#E8457F", pill="#FFE27A", tint="#FDE7EC",
                  line="#EBC6D0", done="#F9CFDA", text="#4A2A38", sheet_header="5B1E3C", sheet_tint="FDE7EC"),
    "sage": dict(bg="#DCEBD3", ink="#22402B", pop="#EF7337", pill="#FFE27A", tint="#E6F0E0",
                 line="#C9D8CF", done="#D3E8C8", text="#33463A", sheet_header="22402B", sheet_tint="E6F0E0"),
    # ready for future products:
    "lavender": dict(bg="#E6DDFB", ink="#33246B", pop="#7A4FE0", pill="#FFE27A", tint="#F1ECFD",
                     line="#D5CBF2", done="#E2D8FA", text="#3B3355", sheet_header="33246B", sheet_tint="F1ECFD"),
    "peach": dict(bg="#FFE0CC", ink="#6B2E14", pop="#F2683C", pill="#FFF0A8", tint="#FFEDE2",
                  line="#F2CDB8", done="#FCD9C4", text="#4E3226", sheet_header="6B2E14", sheet_tint="FFEDE2"),
    "honey": dict(bg="#F7E6C4", ink="#4A3420", pop="#D9822B", pill="#FFF3C4", tint="#FBF1DD",
                  line="#EAD7B4", done="#F3E2BF", text="#4E3D2C", sheet_header="4A3420", sheet_tint="FBF1DD"),
    "sky": dict(bg="#D6EAF8", ink="#173E5C", pop="#2F8FD8", pill="#FFE27A", tint="#E7F2FB",
                line="#C3DCEE", done="#CFE5F5", text="#2C3E4D", sheet_header="173E5C", sheet_tint="E7F2FB"),
    "mint": dict(bg="#CDEFE4", ink="#123F38", pop="#F0566E", pill="#FFE27A", tint="#E3F6EF",
                 line="#BCE2D5", done="#CDEDE1", text="#2A4440", sheet_header="123F38", sheet_tint="E3F6EF"),
}
