Name:		texlive-codeanatomy
Version:	51627
Release:	1
Summary:	Typeset code with annotations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/codeanatomy
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/codeanatomy.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/codeanatomy.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/codeanatomy.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The idea of this Package is to typeset illustrations of pieces
of code with annotations on each single part of code (Code
Anatomy). The origin of this idea are code illustrations from
the book "Computer Science: An Interdisciplinary Approach" from
Robert Sedgewick and Kevin Wayne. The package depends on expl3,
xparse, and TikZ.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/codeanatomy
%{_texmfdistdir}/tex/latex/codeanatomy
%doc %{_texmfdistdir}/doc/latex/codeanatomy

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
