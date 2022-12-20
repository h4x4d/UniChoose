const edu_levels = {
    0: 'Бакалавриат',
    1: 'Специалитет',
    2: 'Магистратура'
}

class Card {
    constructor({
                    department,
                    onDismiss,
                    onLike,
                    onDislike
                }) {
        this.department = department;
        this.onDismiss = onDismiss;
        this.onLike = onLike;
        this.onDislike = onDislike;
        this.#init();
    }

    // private properties
    #offsetX;
    #offsetY;

    #isTouchDevice = () => {
        return (('ontouchstart' in window) ||
            (navigator.maxTouchPoints > 0) ||
            (navigator.msMaxTouchPoints > 0));
    }

    #init = () => {
        console.log(this.department)
        const card = document.createElement('div');
        card.classList.add('card');
        card.classList.add('d-flex');
        card.classList.add('aligns-items-center');
        card.classList.add('justify-content-center');
        card.classList.add('text-center');


        const level_field = document.createElement('h6');
        level_field.innerText = edu_levels[this.department['edu_level']]
        card.append(level_field);

        const name_field = document.createElement('h3');
        name_field.innerText = this.department['name'] + '\n' + this.department['profile_class']
        card.append(name_field);

        const profile_field = document.createElement('h5');
        profile_field.innerText = 'Профиль: ' + this.department['profile']
        card.append(profile_field);

        const entry_field = document.createElement('h4');
        entry_field.innerText = 'Проходной балл: ' + this.department['entry_score'] + '\n(' + this.department['ege_subjects'].join(', ') + ')'
        card.append(entry_field);

        const university_field = document.createElement('h6');
        university_field.innerText = this.department['university_name'] + ' (' + this.department['university_rating'] + ' / ' + this.department['university_rating_count'] + ' оценок)'
        card.append(university_field);

        this.element = card;
        if (this.#isTouchDevice()) {
            this.#listenToTouchEvents();
        } else {
            this.#listenToMouseEvents();
        }
    }

    #listenToTouchEvents = () => {
        this.element.addEventListener('touchstart', (e) => {
            const touch = e.changedTouches[0];
            if (!touch) return;
            const {clientX, clientY} = touch;
            this.startPoint = {x: clientX, y: clientY}
            document.addEventListener('touchmove', this.#handleTouchMove);
            this.element.style.transition = 'transform 0s';
        });

        document.addEventListener('touchend', this.#handleTouchEnd);
        document.addEventListener('cancel', this.#handleTouchEnd);
    }

    #listenToMouseEvents = () => {
        this.element.addEventListener('mousedown', (e) => {
            const {clientX, clientY} = e;
            this.startPoint = {x: clientX, y: clientY}
            document.addEventListener('mousemove', this.#handleMouseMove);
            this.element.style.transition = 'transform 0s';
        });

        document.addEventListener('mouseup', this.#handleMoveUp);

        // prevent card from being dragged
        this.element.addEventListener('dragstart', (e) => {
            e.preventDefault();
        });
    }

    handleMove = (x, y) => {
        this.#offsetX = x - this.startPoint.x;
        this.#offsetY = y - this.startPoint.y;
        const rotate = this.#offsetX * 0.1;
        this.element.style.transform = `translate(${this.#offsetX}px, ${this.#offsetY}px) rotate(${rotate}deg)`;
        // dismiss card
        if (Math.abs(this.#offsetX) > this.element.clientWidth * 0.7) {
            this.dismiss(this.#offsetX > 0 ? 1 : -1);
        }
    }

    // mouse event handlers
    #handleMouseMove = (e) => {
        e.preventDefault();
        if (!this.startPoint) return;
        const {clientX, clientY} = e;
        this.handleMove(clientX, clientY);
    }

    #handleMoveUp = () => {
        this.startPoint = null;
        document.removeEventListener('mousemove', this.#handleMouseMove);
        this.element.style.transform = '';
    }

    // touch event handlers
    #handleTouchMove = (e) => {
        if (!this.startPoint) return;
        const touch = e.changedTouches[0];
        if (!touch) return;
        const {clientX, clientY} = touch;
        this.handleMove(clientX, clientY);
    }

    #handleTouchEnd = () => {
        this.startPoint = null;
        document.removeEventListener('touchmove', this.#handleTouchMove);
        this.element.style.transform = '';
    }

    dismiss = (direction) => {
        if (typeof this.onLike === 'function' && direction === 1) {
            const r = this.onLike(this.department.id);
        }
        if (typeof this.onDislike === 'function' && direction === -1) {
            const r = this.onDislike(this.department.id);
        }
        this.startPoint = null;
        document.removeEventListener('mouseup', this.#handleMoveUp);
        document.removeEventListener('mousemove', this.#handleMouseMove);
        document.removeEventListener('touchend', this.#handleTouchEnd);
        document.removeEventListener('touchmove', this.#handleTouchMove);
        this.element.style.transition = 'transform 1s';
        this.element.style.transform = `translate(${direction * window.innerWidth}px, ${this.#offsetY}px) rotate(${90 * direction}deg)`;
        this.element.classList.add('dismissing');
        setTimeout(() => {
            this.element.remove();
        }, 1000);
        if (typeof this.onDismiss === 'function') {
            this.onDismiss();
        }
    }
}