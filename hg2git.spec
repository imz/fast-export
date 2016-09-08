Name: hg2git
Version: 0.1
Release: alt9

Summary: Mercurial to git converter using git-fast-import
License: GPL
Group: Development/Other

# git://repo.or.cz/fast-export.git
URL: http://repo.or.cz/w/fast-export.git
Source: hg-fast-export-%version-%release.tar
Patch1: hg-fast-export-alt-tags-annotated.patch
Patch2: hg2git-alt-default-branch-name.patch
BuildArch: noarch

%description
This is a work-in-progress for creating a fast and small hg2git script
to initially import and incrementally track mercurial-based repositories
using git. To simplify importing and increase performance, it acts as a
frontend for git-fast-import(1).

%prep
%setup -n hg-fast-export-%version-%release
%patch1 -p1
%patch2 -p1

%install
install -pD -m755 hg2git.py %buildroot%_bindir/hg2git.py
install -pD -m755 hg-fast-export.sh %buildroot%_bindir/hg-fast-export
install -pD -m644 hg-fast-export.py %buildroot%_bindir/hg-fast-export.py

%files
#doc hg-fast-export.txt
%doc README
%_bindir/*

%changelog
* Thu May 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt9
- New snapshot (ALT #30005)

* Tue Apr 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt8
- New snapshot (ALT #30005)

* Wed Nov 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt7
- New snapshot

* Wed Sep 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt6
- New snapshot

* Sat Apr 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt5
- New snapshot

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt4.1
- Rebuild with Python-2.7

* Mon Oct 18 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 0.1-alt4
- Update to c8a45848968a21c3021489a6ba3ab1ffe5ef2a90
- Make package noarch
- Update Url tag

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt3.1
- Rebuilt with python 2.6

* Fri Aug 28 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 0.1-alt3
- New version from raorn (merged with upstream) (Closes: #21276)

* Tue Mar 31 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 0.1-alt2
- Update to working version taken from raorn's git (Closes: #19415, #17668)

* Mon Apr 02 2007 Alexey Tourbin <at@altlinux.ru> 0.1-alt1
- initial revision
