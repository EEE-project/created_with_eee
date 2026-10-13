"""The courses served from their own GitLab Pages projects, listed once; every table the tools need is derived from COURSES.

Another split-off course is one more row; only the hub-card link fix (Makefile, propagate-pages.sh) still names the B1 project. Shell and make use the CLI:
    python3 tools/_split_courses.py projects            GitLab project names, one per line
    python3 tools/_split_courses.py prefix <project>    '/created_with_eee/<root>/', the link prefix of that project's hub pages
    python3 tools/_split_courses.py index-rewrites      FILE<TAB>OLD<TAB>NEW for the GitLab mirror's index.tsv files
"""
import sys
from typing import NamedTuple

PAGES_BASE = "https://eee-project.gitlab.io"  # GitLab Pages host of every project
UNIFIED_ROOT = "/created_with_eee/"  # the unified project's own path prefix, as the hub generator writes links on Codeberg and GitHub


class Course(NamedTuple):
    course_dir: str  # removed from GitLab's unified tree: the whole course
    served_dir: str  # the part of it the project serves, as a path of the unified tree
    project: str  # the GitLab project (bare repo name) that serves it
    root_dir: str  # the directory of the unified tree that is that project's root

    @property
    def dest_prefix(self) -> str:
        """Where served_dir sits inside the project: '' when it is the project's root."""
        return self.served_dir.removeprefix(self.root_dir).strip("/")


_B1 = "modern_greek/b1greeklanguageandculture"
COURSES = (
    Course("ancient_greek/odyssey", "ancient_greek/odyssey", "created-with-eee-odyssey", "ancient_greek/odyssey"),
    Course("ancient_greek/palaestra", "ancient_greek/palaestra/ancient_greek.2026.summer", "created-with-eee-palaestra",
           "ancient_greek/palaestra/ancient_greek.2026.summer"),
    Course(f"{_B1}/kapodistrias", f"{_B1}/kapodistrias", "created-with-eee-b1glc", _B1),
    Course(f"{_B1}/kavafis_ithaki", f"{_B1}/kavafis_ithaki", "created-with-eee-b1glc", _B1),
    Course(f"{_B1}/zorba", f"{_B1}/zorba", "created-with-eee-b1glc", _B1),
)

PROJECTS = tuple(dict.fromkeys(c.project for c in COURSES))
COURSE_DIRS = [c.course_dir for c in COURSES]


def _validate() -> None:
    for c in COURSES:
        if not (c.served_dir == c.root_dir or c.served_dir.startswith(c.root_dir + "/")):
            raise ValueError(f"served_dir must lie inside root_dir: {c}")
    for project in PROJECTS:
        if len({c.root_dir for c in COURSES if c.project == project}) != 1:
            raise ValueError(f"a project has one root directory: {project}")


_validate()


def course_map() -> dict[str, tuple[str, str]]:
    """served_dir -> (project, dest_prefix): where the lesson exports of a course go."""
    return {c.served_dir: (c.project, c.dest_prefix) for c in COURSES}


def hub_map() -> dict[str, tuple[str, str]]:
    """course_map plus each project's root -- the hub whose index.html is the project's front page."""
    out: dict[str, tuple[str, str]] = {}
    for c in COURSES:
        out.setdefault(c.root_dir, (c.project, ""))
        out[c.served_dir] = (c.project, c.dest_prefix)
    return out


def scope_map() -> dict[str, tuple[str, str]]:
    """course_dir -> (project, root_dir): the courses GitLab's unified tree must not hold, and the project its links go to instead."""
    return {c.course_dir: (c.project, c.root_dir) for c in COURSES}


def gitlab_overrides() -> dict[str, str]:
    """Root-relative hub link (as written on Codeberg and GitHub) -> the project's own GitLab Pages URL, per project root."""
    return {f"{UNIFIED_ROOT}{c.root_dir}/": f"{PAGES_BASE}/{c.project}/" for c in COURSES}


def hub_link_prefix(project: str) -> str:
    """The absolute path prefix the hub cards of a project's courses carry on Codeberg and GitHub."""
    for c in COURSES:
        if c.project == project:
            return f"{UNIFIED_ROOT}{c.root_dir}/"
    raise KeyError(project)


def index_rewrites() -> list[tuple[str, str, str]]:
    """(index.tsv, old, new) per course: its root-relative back link becomes the project's absolute GitLab Pages URL."""
    return [
        (f"{c.served_dir}/index.tsv", f"{UNIFIED_ROOT}{c.served_dir}/", f"{PAGES_BASE}/{c.project}/{c.dest_prefix + '/' if c.dest_prefix else ''}")
        for c in COURSES
    ]


def main(argv: list[str]) -> int:
    if argv == ["projects"]:
        for project in PROJECTS:
            print(project)
    elif len(argv) == 2 and argv[0] == "prefix":
        try:
            print(hub_link_prefix(argv[1]))
        except KeyError:
            print(f"error: not a split project: {argv[1]} (known: {', '.join(PROJECTS)})", file=sys.stderr)
            return 1
    elif argv == ["index-rewrites"]:
        for row in index_rewrites():
            print("\t".join(row))
    else:
        print(__doc__, file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
