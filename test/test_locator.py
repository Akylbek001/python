from appium.webdriver.common.appiumby import AppiumBy


def locator():
    locator_dict = {
        'authorization': {
            'permission_allow_button': (AppiumBy.ID, 'com.android.packageinstaller:id/permission_allow_button'),
            'close': (AppiumBy.ACCESSIBILITY_ID, 'Маска'),
            'login/registration': (AppiumBy.ACCESSIBILITY_ID, "Вход/Регистрация"),
            'login_text_editor2': (AppiumBy.XPATH, "//android.widget.EditText[@text='+7']"),
            'pass_text_editor': (AppiumBy.XPATH, '//android.widget.EditText[@index="1"]'),
            'login_button': (AppiumBy.ACCESSIBILITY_ID, 'Войти'),
            'password_button': (AppiumBy.ACCESSIBILITY_ID, "2"),
            'open_new_depoz_or_schet': (AppiumBy.ACCESSIBILITY_ID, 'Открыть новый депозит или счет')
        },
        'locator_butt': {
            'button_next': (AppiumBy.ACCESSIBILITY_ID, "Продолжить"),
            'button_vybrat': (AppiumBy.ACCESSIBILITY_ID, 'Выбрать'),
            'checkBox_zayavlenie_soglasie': (AppiumBy.XPATH, '//android.widget.ScrollView/android.widget.ImageView[1]'),
            'button_podtverdit': (AppiumBy.ACCESSIBILITY_ID, "Подтвердить"),
            'button_prodolzhit': (AppiumBy.ACCESSIBILITY_ID, "Подписать"),
            'button_otpravit': (AppiumBy.ACCESSIBILITY_ID, "Отправить"),
            'button_na_glavnyu': (AppiumBy.ACCESSIBILITY_ID, "На главную"),
            'button_close': (AppiumBy.ACCESSIBILITY_ID, "Закрыть"),
            'button_x': (AppiumBy.XPATH, '//android.widget.ImageView[@index="0"]'),
            'CheckBox': (AppiumBy.XPATH, '//android.widget.CheckBox'),
        },
        'locator_dep': {
            'vybor_depozit': (AppiumBy.ACCESSIBILITY_ID, 'Депозит\nот 04.03.2022\n2 000 ₸'),
        },
        'locator_obedinenie_depozita': {
            'obedinenie_depozita': (AppiumBy.ACCESSIBILITY_ID, "Объединение депозита")
        },
        'locator_prisvoenie': {
            'prisvoenie_gos_premi': (AppiumBy.ACCESSIBILITY_ID, "Присвоение Гос. Премии"),
            'dep_s_gos_premi': (AppiumBy.ACCESSIBILITY_ID, "Депозит\n  от \n15-2022-0003668-1523\nГос. премия\nВыгодный\nНакоплено\n2 000 ₸\nПрогнозируемая премия\n400 ₸"),

        },
        'locator_uslovia': {
            'zayvlenie_o_gos_premi': (AppiumBy.ACCESSIBILITY_ID, 'Заявление О Начислении Премии Государства'),
        },
        'locator_kredit': {
            'vybor_kredita': (AppiumBy.ACCESSIBILITY_ID, "Займ от 05.02.2021\nF00804-0200-2021\nВыплачено\n38.0%"),
        },
        'locator_izm_data_platezha': {
            'izmenit_data_platezha': (AppiumBy.ACCESSIBILITY_ID, "Изменение даты платежа"),
            'maska_komissiya': (AppiumBy.ACCESSIBILITY_ID, "Изменение даты платежа"),
            'new_payment_date': (AppiumBy.ACCESSIBILITY_ID, '10'),
            'button_otmena': (AppiumBy.ACCESSIBILITY_ID,
                              'Изменение даты платежа Подтверждаете изменение даты ежемесячного платежа по займу с '
                              '“24” на “10”? Отмена'),
        },
        'locator_tek_schet': {
            'tek_schet_vhod': (AppiumBy.ACCESSIBILITY_ID, "Текущий счет\n3 010 143,64 ₸")
        },
        'locator_pdp': {
            'polnoe_dosrochnoe_pogoshenie': (AppiumBy.ACCESSIBILITY_ID, "Полное досрочное погашение"),

        },
        'locator_menu': {
            'personal_data': (AppiumBy.ACCESSIBILITY_ID, 'Личные данные'),
            'my_applications': (AppiumBy.ACCESSIBILITY_ID, 'Мои заявки'),
            'my_doc': (AppiumBy.ACCESSIBILITY_ID, 'Мои документы'),
            'my_requests': (AppiumBy.ACCESSIBILITY_ID, 'Мои обращения'),
            'zapis_v_bank': (AppiumBy.ACCESSIBILITY_ID, 'Запись в отделение'),
            'get_spravki': (AppiumBy.ACCESSIBILITY_ID, 'Получить справку'),
            'about_the_application': (AppiumBy.ACCESSIBILITY_ID, 'О приложении'),
        },
        'locator_vkladok': {
            'menu': (AppiumBy.ACCESSIBILITY_ID, "Меню\nВкладка 4 из 4"),
            'my_bank': (AppiumBy.ACCESSIBILITY_ID, "Мой Банк\nВкладка 2 из 4"),
            'glavnaya': (AppiumBy.ACCESSIBILITY_ID, "Главная\nВкладка 1 из 4"),
        }
    }
    return locator_dict
