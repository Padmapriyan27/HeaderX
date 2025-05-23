import httpx
from rich.text import Text
from typing import Dict, Tuple, List


class HeaderAnalyzer:

    HeaderCategory = dict[str, str]

    Header_Classification: HeaderCategory = {
        "Accept": "Standard",
        "Accept-CH": "Standard",
        "Accept-Encoding": "Standard",
        "Accept-Language": "Standard",
        "Accept-Patch": "Standard",
        "Accept-Post": "Standard",
        "Accept-Ranges": "Standard",
        "Access-Control-Allow-Credentials": "Standard",
        "Access-Control-Allow-Headers": "Standard",
        "Access-Control-Allow-Methods": "Standard",
        "Access-Control-Allow-Origin": "Standard",
        "Access-Control-Expose-Headers": "Standard",
        "Access-Control-Max-Age": "Standard",
        "Access-Control-Request-Headers": "Standard",
        "Access-Control-Request-Method": "Standard",
        "Age": "Standard",
        "Allow": "Standard",
        "Alt-Svc": "Standard",
        "Alt-Used": "Standard",
        "Attribution-Reporting-Eligible": "Experimental",
        "Attribution-Reporting-Register-Source": "Experimental",
        "Attribution-Reporting-Register-Trigger": "Experimental",
        "Authorization": "Standard",
        "Available-Dictionary": "Experimental",
        "Cache-Control": "Standard",
        "Clear-Site-Data": "Standard",
        "Connection": "Standard",
        "Content-Digest": "Standard",
        "Content-Disposition": "Standard",
        "Content-DPR": "Non-std-dep",
        "Content-Encoding": "Standard",
        "Content-Language": "Standard",
        "Content-Length": "Standard",
        "Content-Location": "Standard",
        "Content-Range": "Standard",
        "Content-Security-Policy": "Security",
        "Content-Security-Policy-Report-Only": "Security",
        "Content-Type": "Standard",
        "Cookie": "Standard",
        "Critical-CH": "Experimental",
        "Cross-Origin-Embedder-Policy": "Security",
        "Cross-Origin-Opener-Policy": "Security",
        "Cross-Origin-Resource-Policy": "Security",
        "Date": "Standard",
        "Device-Memory": "Experimental",
        "Dictionary-ID": "Experimental",
        "DNT": "Non-std-dep",
        "Downlink": "Experimental",
        "DPR": "Non-std-dep",
        "Early-Data": "Experimental",
        "ECT": "Experimental",
        "ETag": "Standard",
        "Expect": "Standard",
        "Expect-CT": "Deprecated",
        "Expires": "Standard",
        "Forwarded": "Standard",
        "From": "Standard",
        "Host": "Standard",
        "If-Match": "Standard",
        "If-Modified-Since": "Standard",
        "If-None-Match": "Standard",
        "If-Range": "Standard",
        "If-Unmodified-Since": "Standard",
        "Keep-Alive": "Standard",
        "Last-Modified": "Standard",
        "Link": "Standard",
        "Location": "Standard",
        "Max-Forwards": "Standard",
        "NEL": "Experimental",
        "No-Vary-Search": "Experimental",
        "Observe-Browsing-Topics": "Experimental",
        "Origin": "Standard",
        "Origin-Agent-Cluster": "Standard",
        "Permissions-Policy": "Experimental",
        "Pragma": "Deprecated",
        "Prefer": "Standard",
        "Preference-Applied": "Standard",
        "Priority": "Standard",
        "Proxy-Authenticate": "Standard",
        "Proxy-Authorization": "Standard",
        "Range": "Standard",
        "Referer": "Standard",
        "Referrer-Policy": "Security",
        "Refresh": "Standard",
        "Report-To": "Non-std-dep",
        "Reporting-Endpoints": "Standard",
        "Repr-Digest": "Standard",
        "Retry-After": "Standard",
        "RTT": "Experimental",
        "Save-Data": "Experimental",
        "Sec-Browsing-Topics": "Experimental",
        "Sec-CH-Prefers-Color-Scheme": "Experimental",
        "Sec-CH-Prefers-Reduced-Motion": "Experimental",
        "Sec-CH-Prefers-Reduced-Transparency": "Experimental",
        "Sec-CH-UA": "Experimental",
        "Sec-CH-UA-Arch": "Experimental",
        "Sec-CH-UA-Bitness": "Experimental",
        "Sec-CH-UA-Form-Factors": "Experimental",
        "Sec-CH-UA-Full-Version": "Deprecated",
        "Sec-CH-UA-Full-Version-List": "Experimental",
        "Sec-CH-UA-Mobile": "Experimental",
        "Sec-CH-UA-Model": "Experimental",
        "Sec-CH-UA-Platform": "Experimental",
        "Sec-CH-UA-Platform-Version": "Experimental",
        "Sec-CH-UA-WoW64": "Experimental",
        "Sec-Fetch-Dest": "Standard",
        "Sec-Fetch-Mode": "Standard",
        "Sec-Fetch-Site": "Standard",
        "Sec-Fetch-User": "Standard",
        "Sec-GPC": "Experimental",
        "Sec-Purpose": "Standard",
        "Sec-Speculation-Tags": "Experimental",
        "Sec-WebSocket-Accept": "Standard",
        "Sec-WebSocket-Extensions": "Standard",
        "Sec-WebSocket-Key": "Standard",
        "Sec-WebSocket-Protocol": "Standard",
        "Sec-WebSocket-Version": "Standard",
        "Server": "Standard",
        "Server-Timing": "Standard",
        "Service-Worker": "Standard",
        "Service-Worker-Allowed": "Standard",
        "Service-Worker-Navigation-Preload": "Standard",
        "Set-Cookie": "Standard",
        "Set-Login": "Standard",
        "SourceMap": "Standard",
        "Speculation-Rules": "Experimental",
        "Strict-Transport-Security": "Security",
        "Supports-Loading-Mode": "Experimental",
        "TE": "Standard",
        "Timing-Allow-Origin": "Standard",
        "Tk": "Non-std-dep",
        "Trailer": "Standard",
        "Transfer-Encoding": "Standard",
        "Upgrade": "Standard",
        "Upgrade-Insecure-Requests": "Standard",
        "Use-As-Dictionary": "Experimental",
        "User-Agent": "Standard",
        "Vary": "Standard",
        "Via": "Standard",
        "Viewport-Width": "Non-std-dep",
        "Want-Content-Digest": "Standard",
        "Want-Repr-Digest": "Standard",
        "Warning": "Deprecated",
        "Width": "Non-std-dep",
        "WWW-Authenticate": "Standard",
        "X-Content-Type-Options": "Security",
        "X-DNS-Prefetch-Control": "Non-standard",
        "X-Forwarded-For": "Non-standard",
        "X-Forwarded-Host": "Non-standard",
        "X-Forwarded-Proto": "Non-standard",
        "X-Frame-Options": "Security",
        "X-Permitted-Cross-Domain-Policies": "Non-standard",
        "X-Powered-By": "Non-standard",
        "X-Robots-Tag": "Non-standard",
        "X-XSS-Protection": "Non-std-dep"
    }

    HEADER_STYLE_MAP = {
        "Standard": "bold bright_white",
        "Security": "bold bright_green",
        "Experimental": "bold bright_cyan",
        "Deprecated": "bold bright_red",
        "Non-std-dep": "bold orange_red1",
        "Non-standard": "bold bright_magenta",
        "Unknown": "dim",
    }

    def __init__(self):
        self.NORMALIZED_HEADER_CLASSIFICATION = {
            key.lower(): value for key, value in self.Header_Classification.items()
        }

    def format_raw_headers(self, headers: dict, start_line: str) -> str:
        lines = [start_line] + [f"{k}: {v}" for k, v in headers.items()]
        return "\n".join(lines)

    async def fetch_headers(self, url: str) -> Tuple[str, str]:
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "https://" + url
        try:
            async with httpx.AsyncClient(follow_redirects=True, timeout=10) as client:
                response = await client.get(url)
        except httpx.RequestError as e:
            raise RuntimeError(f"Failed to fetch headers: {e}") from e

        request_headers = dict(response.request.headers)
        response_headers = dict(response.headers)

        request_line = f"{response.request.method} {response.request.url.path or '/'} HTTP/1.1"
        raw_request = self.format_raw_headers(request_headers, request_line)

        status_line = f"{response.http_version} {response.status_code} {response.reason_phrase}"
        raw_response = self.format_raw_headers(response_headers, status_line)

        return raw_request, raw_response

    def analyze_headers(self, headers: Dict[str, str]) -> List[Tuple[str, str, str]]:
        analysis = []
        for key, value in headers.items():
            classification = self.NORMALIZED_HEADER_CLASSIFICATION.get(key.strip().lower(), "Unknown")
            analysis.append((key, value, classification))
        return sorted(analysis, key=lambda x: x[0].lower())

    def highlight_headers(self, raw: str, is_response: bool = False) -> Text:
        highlighted = Text()
        for line in raw.strip().splitlines():
            if ": " in line:
                key, value = line.split(": ", 1)
                classification = self.NORMALIZED_HEADER_CLASSIFICATION.get(key.strip().lower(), "Unknown")
                style = self.HEADER_STYLE_MAP.get(classification, "dim")

                highlighted.append(f"{key}", style=style)
                highlighted.append(": ")
                highlighted.append(f"{value}\n", style="bright_white" if not is_response else "bright_yellow")
            else:
                highlighted.append(line + "\n", style="bold bright_green")
        return highlighted
