import vobject

with open('C:\D\PYReposit\Test\My Experiments\Карточки vCard из iCloud.vcf', 'r', encoding='utf-8') as inf:
    indata = inf.read()
    vc = vobject.readComponents(indata)
    vo = next(vc, None)
    while vo is not None:
        with open('contiph.txt', 'a', encoding='utf-8') as f:
            f.write(vo.fn.value + ' ' + vo.tel.value + '\n')
        vo = next(vc, None)







