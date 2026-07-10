%global tl_name codeanatomy
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.5~Beta
Release:	%{tl_revision}.1
Summary:	Typeset code with annotations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/codeanatomy
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/codeanatomy.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/codeanatomy.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/codeanatomy.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The idea of this Package is to typeset illustrations of pieces of code
with annotations on each single part of code (Code Anatomy). The origin
of this idea are code illustrations from the book "Computer Science: An
Interdisciplinary Approach" from Robert Sedgewick and Kevin Wayne. The
package depends on expl3, xparse, and TikZ.

