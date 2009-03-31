Name: hg2git
Version: 0.1
Release: alt1

Summary: Mercurial to git converter using git-fast-import
License: GPL
Group: Development/Other

URL: http://repo.or.cz/w/hg2git.git
Packager: Vladimir V. Kamarzin <vvk@altlinux.org>
Source: %name-%version-%release.tar

%description
This is a work-in-progress for creating a fast and small hg2git script
to initially import and incrementally track mercurial-based repositories
using git. To simplify importing and increase performance, it acts as a
frontend for git-fast-import(1).

%prep
%setup -q -n %name-%version-%release

%install
install -pD -m755 hg2git.py %buildroot%_bindir/hg2git.py
install -pD -m755 hg-fast-export.sh %buildroot%_bindir/hg-fast-export
install -pD -m644 hg-fast-export.py %buildroot%_bindir/hg-fast-export.py

%files
%doc hg-fast-export.txt
%_bindir/*

%changelog
* Mon Apr 02 2007 Alexey Tourbin <at@altlinux.ru> 0.1-alt1
- initial revision
