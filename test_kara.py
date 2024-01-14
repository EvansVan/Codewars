from kara import length_of_railway

def test_one():
    assert length_of_railway('呜呜呜哐当哐当哐当哐当哐当呜呜呜哐当哐当哐当哐当哐当') == 150

def test_two():
    assert length_of_railway('呜呜呜哐当哐当哐当哐当哐当呜呜呜哐当哐当哐当哐当哐当呜呜呜哐当哐当哐当哐当哐当呜呜呜哐当哐当哐当哐当哐当') == 300

def test_three():
    assert length_of_railway('呜呜呜哐当哐当面包饮料矿泉水了啊，哐当桶面火腿肠茶叶蛋了啊哐当哐当呜呜呜哐当哐当哐当北京站到了，下车的旅客请带好您的行李，准备下车哐当哐当') == 150

def test_four():
    assert length_of_railway('哐当哐当哐当哐当服哐当哐当')== 60
