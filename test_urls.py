import urllib.request

urls = [
    "https://capsule-render.vercel.app/api?type=waving&color=timeGradient&height=250&section=header&text=Hi,%20I'm%20Raj%20👋&fontSize=60&fontAlignY=38&desc=Full-Stack%20Developer%20%26%20SIH%202025%20Winner&descAlignY=55&descAlign=50&animation=twinkling",
    "https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=36BCF7&center=true&vCenter=true&width=800&lines=Building+AI-powered+applications+for+social+impact",
    "https://github-readme-stats.vercel.app/api/pin/?username=Rajj-c&repo=SIH-FINAL-IMPS&theme=tokyonight&show_icons=true",
    "https://skillicons.dev/icons?i=js,ts,react,nextjs,python,nodejs,express,mongodb,gcp,docker,git,github&perline=6",
    "https://github-readme-stats.vercel.app/api?username=Rajj-c&theme=tokyonight&hide_border=false&include_all_commits=true&count_private=true&show_icons=true",
    "https://github-readme-streak-stats.herokuapp.com/?user=Rajj-c&theme=tokyonight&hide_border=false"
]

for u in urls:
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
        r = urllib.request.urlopen(req)
        print(f"OK: {r.status} -> {u[:60]}")
    except Exception as e:
        print(f"ERR: {e} -> {u[:60]}")
