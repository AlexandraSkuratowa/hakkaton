
import openai
import time
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


openai.api_key = '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'  # зарегали ключ доступа
# создаем функциб генерации темы для статьи

for i in range(10):
    if i == 0:
        def generate_tema(text):
            tema = openai.Completion.create(
                prompt=text,
                engine='gpt-3.5-turbo-instruct',  # это выбор модели ИИ  с которой мы будем работать
                max_tokens=100,
                temperature=0.5,
                n=1,
                stop=('.'),
                timeout=10
            )

            return tema.choices[0].text  # Возвращаем сгенерированную тему


        tema = generate_tema('Придумай название статьи в области: Государство и право или Юридические науки.')
        print(tema)

    elif i == 1:

        def generate_metodolog(text):
            metodolog = openai.Completion.create(
                prompt=text,
                engine='gpt-3.5-turbo-instruct',
                # max_tokens=1500,
                temperature=1,
                n=1,
                timeout=40,
                stop=('.')
            )

            def timer(seconds):
                start_time = time.time()
                end_time = start_time + seconds

                while time.time() < end_time:
                    remaining_time = int(end_time - time.time())
                    time.sleep(1)

            # Запустить таймер на 20 секунд
            timer(20)

            return metodolog.choices[0].text


        metodolog = generate_metodolog(
            'Напиши один метод исследования на тему:' + tema + 'который больше всего подойдет, но исключи возможность интервью и опросов')
    elif i == 2:
        def generate_issledov(text):
            issledov = openai.Completion.create(
                prompt=text,
                engine='gpt-3.5-turbo-instruct',
                # max_tokens=1500,
                temperature=1,
                n=1,
                stop=('.'),
                timeout=40
            )

            def timer(seconds):
                start_time = time.time()
                end_time = start_time + seconds

                while time.time() < end_time:
                    remaining_time = int(end_time - time.time())
                    time.sleep(1)

            # Запустить таймер на 20 секунд
            timer(20)

            return issledov.choices[0].text


        issledov = generate_issledov(
            'Используя метод' + metodolog + 'напиши исследование на эту тему для научной статьи')
    elif i == 3:
        def generate_isledov(text):
            isledov = openai.Completion.create(
                prompt=text,
                engine='gpt-3.5-turbo-instruct',
                # max_tokens=1500,
                temperature=1,
                n=1,
                stop=('.'),
                timeout=60
            )

            def timer(seconds):
                start_time = time.time()
                end_time = start_time + seconds

                while time.time() < end_time:
                    remaining_time = int(end_time - time.time())
                    time.sleep(1)

            # Запустить таймер на 20 секунд
            timer(20)

            return isledov.choices[0].text


        isledov = generate_isledov('Напиши научное дополнение к тексту ' + issledov)
    elif i == 4:
        def generate_isledovas(text):
            isledovas = openai.Completion.create(
                prompt=text,
                engine='gpt-3.5-turbo-instruct',
                # max_tokens=1500,
                temperature=1,
                n=1,
                stop=('.'),
                timeout=60
            )

            def timer(seconds):
                start_time = time.time()
                end_time = start_time + seconds

                while time.time() < end_time:
                    remaining_time = int(end_time - time.time())
                    time.sleep(1)

            # Запустить таймер на 20 секунд
            timer(20)

            return isledovas.choices[0].text


        isledovas = generate_isledovas(
            'Напиши дополнение к тексту ' + isledov + 'Добавь личного исследовательского опыта')

        telo = metodolog + issledov + isledovas
    elif i == 5:
        def generate_result(text):
            result = openai.Completion.create(
                prompt=text,
                engine='gpt-3.5-turbo-instruct',
                # max_tokens=1500,
                temperature=1,
                n=1,
                stop=('.'),
                timeout=60
            )

            def timer(seconds):
                start_time = time.time()
                end_time = start_time + seconds

                while time.time() < end_time:
                    remaining_time = int(end_time - time.time())
                    time.sleep(1)

            # Запустить таймер на 20 секунд
            timer(20)

            return result.choices[0].text


        result = generate_result('Какие результаты были получены в ходе этого исследования' + telo)

    elif i == 6:
        def generate_lit(text):
            lit = openai.Completion.create(
                prompt=text,
                engine='gpt-3.5-turbo-instruct',
                max_tokens=1500,
                temperature=1,
                n=1,
                stop=('.'),
                timeout=60
            )

            def timer(seconds):
                start_time = time.time()
                end_time = start_time + seconds

                while time.time() < end_time:
                    remaining_time = int(end_time - time.time())
                    time.sleep(1)

            # Запустить таймер на 20 секунд
            timer(20)

            return lit.choices[0].text


        lit = generate_lit('Составь список литературы на основе которого ты написал этот текст ' + telo)

    elif i == 7:
        def generate_vivod(text):
            vivod = openai.Completion.create(
                prompt=text,
                engine='gpt-3.5-turbo-instruct',
                max_tokens=1500,
                temperature=1,
                n=1,
                stop=('.'),
                timeout=60
            )

            def timer(seconds):
                start_time = time.time()
                end_time = start_time + seconds

                while time.time() < end_time:
                    remaining_time = int(end_time - time.time())
                    time.sleep(1)

            # Запустить таймер на 20 секунд
            timer(30)

            return vivod.choices[0].text


        vivod = generate_vivod('Какие выводы можно получить из данного текста' + telo + result)
    elif i == 8:
        def generate_anatation(text):
            anatation = openai.Completion.create(
                prompt=text,
                engine='gpt-3.5-turbo-instruct',
                max_tokens=1500,
                temperature=1,
                n=1,
                stop=('.'),
                timeout=60
            )

            def timer(seconds):
                start_time = time.time()
                end_time = start_time + seconds

                while time.time() < end_time:
                    remaining_time = int(end_time - time.time())
                    time.sleep(1)

            # Запустить таймер на 30 секунд
            timer(30)

            return anatation.choices[0].text


        anatation = generate_anatation('Напиши анотацию к данному тексту' + telo + result)
    elif i == 9:
        def generate_vvidenie(text):
            vvidenie = openai.Completion.create(
                prompt=text,
                engine='gpt-3.5-turbo-instruct',

                max_tokens=1500,
                temperature=1,
                n=1,
                stop=('.'),
                timeout=60
            )

            def timer(seconds):
                start_time = time.time()
                end_time = start_time + seconds

                while time.time() < end_time:
                    remaining_time = int(end_time - time.time())
                    time.sleep(1)

            # Запустить таймер на 30 секунд
            timer(30)

            return vvidenie.choices[0].text


        vvidenie = generate_vvidenie('Напиши введение к данному тексту' + telo + result + anatation + vivod)
        statia = anatation + vvidenie + metodolog + telo + result + vivod + lit
        print(statia)
    elif i == 10:
          def create_pdf(text):
              canvas = Canvas("01_01.pdf")
              canvas.drawString(72, 72, statia)
              canvas.save()










